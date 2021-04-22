from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, generics, views
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import jwt
import json
import math
import random
import requests
from django.db import connection

from .serializers import *
from .validations import *
from .models import UserAccoutDetail, OtpAuthenticationSystem
from .services import *
from djangoproject_todolist import settings

# Create your views here.


class SignUp_View(GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        Validation_Response = SignUpView_Validation(request)
        if Validation_Response:
            return Response(Validation_Response, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get("password") != request.data.get("confirm_password"):
            Message = "Password Not Match"
            return Response(Message, status=status.HTTP_400_BAD_REQUEST)

        Serializer_Response = SignUpFinalSerializer(data=request.data)
        if Serializer_Response.is_valid():
            print("flag", Serializer_Response)
            Serializer_Response.save()
            Message = "Sign Up Successful"
            data = {
                "Message": Message,
                "data": request.data
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response("valid", status=status.HTTP_200_OK)


class SendEmailView(GenericAPIView):

    serializer_class = EmailResponseSerializer

    def post(self, request):
        # print("flag 1")
        Validation_response = SendEmailView_Validation(request)
        if Validation_response:
            return Response(Validation_response, status=status.HTTP_400_BAD_REQUEST)
        try:
            email_Response = UserAccoutDetail.objects.get(
                email=request.data.get("email"))
            print(email_Response)
        except:
            Message = "Email Id Does Not Found, Enter Valid Email Id"
            return Response(Message, status=status.HTTP_400_BAD_REQUEST)

        print("data:", email_Response)
        token = RefreshToken.for_user(email_Response).access_token

        current_site = get_current_site(request).domain

        absoluteUrl = 'http://'+current_site + \
            "/api/VerifyEmail/?token="+str(token)
        email_body = "Hi " + email_Response.username + \
            " Use link below to verify Account :\n"+absoluteUrl
        data = {"email_body": email_body, 'to_email': email_Response.email,
                'email_subject': 'Verify Your Account'}
        Email_Response = Util.send_email(data)
        print(Email_Response)
        if Email_Response == 200:
            Message = "Email Send SucessFully"
            data = {
                "Message": Message,
                "data": data
            }
            print("status mail 200")
            return Response(data, status=status.HTTP_200_OK)
        else:
            Message = "Email Send Unsucessfully"
            data = {
                "Message": Message,
                "data": data
            }
            print("Status mail 500")
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyEmailView(views.APIView):

    # serializer_class = EmailAccountVarificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, options={"verify_signature": False})

            data = UserAccoutDetail.objects.get(id=payload['user_id'])
            if not data.is_verified:
                data.is_verified = True
                print("User is_verified 1 =", data.is_verified)
                data.save()
                serializer = FetchUserAllData(data, many=False)
                Message = "User Account Varification"
                data = {
                    "Message": Message,
                    "data": serializer.data
                }
                print("Response :", data)
                return Response(data, status=status.HTTP_200_OK)
            else:
                Message = "Account Already Varified"
                serializer = SignUpSerializer(data, many=False)
                data = {
                    "Message": Message,
                    "data": serializer.data
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except jwt.ExpiredSignatureError as identifier:
            data = {
                "Error": "JWT Signature Error"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            data = {
                "Error": "Jwt Decode Token Error"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(generics.GenericAPIView):

    serializer_class = LoginSerializers

    def post(self, request):
        print("flag 1")
        Validation_response = LoginEmailview_Validation(request)

        if Validation_response:
            return Response(Validation_response, status=status.HTTP_400_BAD_REQUEST)

        try:
            print("flag 2")
            email_Response = UserAccoutDetail.objects.get(
                email=request.data.get("email"))
            print("Response = ", email_Response.id,
                  "Password =", email_Response.password)
            if email_Response.password != request.data.get("password"):
                Message = "Incurrect Password"
                return Response(Message, status=status.HTTP_400_BAD_REQUEST)

            print("flag 3")
            serializer = FetchUserAllData(email_Response, many=False)
            print("Token Creation- Email =", request.data.get("email"),
                  " Password =", request.data.get("password"))
            print("email_Response.id :", email_Response.id,
                  "email_Response.username :", email_Response.username)
            token_Response = TokenServices.generateToken(email_Response.id, email_Response.username,
                                                         request.data.get("email"), request.data.get("password"))
            print("token_Response :", token_Response)
            if token_Response == 500:
                Message = "Token Generation Error"
                return Response(Message, status=status.HTTP_400_BAD_REQUEST)

            print("Access Token =", token_Response['AccessToken'])

            data = {
                "Message :": "Login SuccessFully",
                "data :": request.data,
                "Access Token :": str(token_Response['AccessToken'])
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)

            # data = {
            #     "Message": "Login Unsuccessfull",
            #     "data": request.data
            # }
            # return Response(data, status=status.HTTP_404_NOT_FOUND)
        except:
            Message = "Email Id Does Not Found, Enter Valid Email Id"
            return Response(Message, status=status.HTTP_400_BAD_REQUEST)

        return Response("Valid", status=status.HTTP_200_OK)


class GenerateOtpApiView(GenericAPIView):
    serializer_class = GenerateOtpSerializer

    def post(self, request):
        try:
            otp_count = None
            MobileId_Response = MobileId_Validation(request)
            if MobileId_Response:
                return Response(MobileId_Response, status=status.HTTP_400_BAD_REQUEST)

            # Get Mobile Number Detail
            mobile_Number = request.data.get('mobileNumber')
            try:

                Result = UserAccoutDetail.objects.get(
                    mobileNumber=mobile_Number)
                Result_Response = FetchUserAllData(Result,  many=False)
                try:
                    c = connection.cursor()
                    c.execute(
                        "SELECT Otp_Created_Count FROM system_authentication_otpauthenticationsystem WHERE mobileNumber=%s", [mobile_Number])
                    user = c.fetchall()
                    otp_count = user[0][0]
                except:
                    otp_count = 0
                    pass

            except Exception:
                Message = "Mobile Number Not Present"
                return Response(Message, status=status.HTTP_400_BAD_REQUEST)
            ########

            # Create 6 digit Otp Number

            OtpGenerate_Result = OTPServices.GenerateOtpNumber()
            if OtpGenerate_Result['status'] == 500:
                return Response(OtpGenerate_Result, status=status.HTTP_417_EXPECTATION_FAILED)
            otp_variable = OtpGenerate_Result['otp']

            #####
            # Send Otp To Register Number
            try:
                Sendotp_Result = OTPServices.SendOtp(otp_variable, request)
                if Sendotp_Result['status'] == 500:
                    return Response(Sendotp_Result, status=status.HTTP_417_EXPECTATION_FAILED)
                ########

                # Save Otp Detail of Register Numeber To OTP Table
                otp_count += 1
                try:
                    if otp_count == 1:
                        # Otp send First Time Condition
                        Otp_data = {
                            "user_id": Result_Response.data['id'],
                            "mobileNumber": mobile_Number,
                            "Otp": otp_variable,
                            "Otp_Created_Count": otp_count
                        }
                        serializers = OtpDetailSerializer(data=Otp_data)
                        if serializers.is_valid():
                            serializers.save()
                        else:
                            return Response("Otp Table Record Not Created", status=status.HTTP_400_BAD_REQUEST)
                    else:
                        # Otp send More than One Time condition
                        c = connection.cursor()
                        c.execute(
                            "UPDATE system_authentication_otpauthenticationsystem SET Otp = %s , Otp_Created_Count = %s WHERE mobileNumber=%s", [otp_variable, otp_count, mobile_Number])
                except:
                    Message = "OTP Database Error Occur"
                    data = {
                        "Message": Message,
                        "data": request.data
                    }
                    return Response(data, status=status.HTTP_417_EXPECTATION_FAILED)

                Message = "Otp Send Sucessfully"
                data = {
                    "Message": Message,
                    "data": request.data
                }
                return Response(data, status=status.HTTP_201_CREATED)
            except:
                return Response("Generate OTP server Error", status=status.HTTP_417_EXPECTATION_FAILED)

            ######################
        except Exception:
            Message = "Internel Server Error"
            return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OtpVerificationView(GenericAPIView):

    serializer_class = OtpVerificationSerializer

    def post(self, request):
        try:
            c = connection.cursor()
            Validation_Result = OtpVerificationValidation(request)
            print(Validation_Result)
            if Validation_Result:
                return Response(Validation_Result, status=status.HTTP_400_BAD_REQUEST)
            Mobile_Number = request.data.get("mobileNumber")
            Request_otp = request.data.get("otp")
            print("Mobile Number :", Mobile_Number)
            try:
                c.execute(
                    "SELECT * FROM system_authentication_otpauthenticationsystem WHERE mobileNumber=%s", [Mobile_Number])
                user = c.fetchall()
                print("User :", user)
                print("Index :", user[0][0])

                try:
                    c.execute(
                        "SELECT Otp FROM system_authentication_otpauthenticationsystem WHERE mobileNumber=%s", [Mobile_Number])
                    user = c.fetchall()
                    otp = user[0][0]
                    print("Database Otp :", otp)
                    print("User Otp :", Request_otp)
                    print(int(otp) == int(Request_otp))
                    if otp == int(Request_otp):
                        Message = "Otp Match"
                        return Response(Message, status=status.HTTP_202_ACCEPTED)
                    Message = "Invalid Otp"
                    return Response(Message, status=status.HTTP_400_BAD_REQUEST)
                except:
                    pass

            except:
                Message = "Mobile Number Not Found"
                return Response(Message, status=status.HTTP_406_NOT_ACCEPTABLE)
            # return Response("Valid")
        except Exception:
            Message = "Internel Server Error"
            return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
