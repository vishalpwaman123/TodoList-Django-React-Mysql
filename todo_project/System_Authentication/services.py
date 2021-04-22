from django.core.mail import EmailMessage
import os
from decouple import config
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.contrib import auth
import jwt
import json
from datetime import datetime, timedelta
from django.utils import timezone
import math
import random
import requests
from djangoproject_todolist import settings
# from .models import User


class Util:
    Response = None

    @staticmethod
    def send_email(data):
        try:
            print(config("EMAIL_HOST_USER"))
            print(config("EMAIL_HOST_PASSWORD"))
            print(str(data['email_subject'])+" " +
                  str(data['email_body'])+" "+str(data['to_email']))

            email = EmailMessage(subject=data['email_subject'],
                                 body=data['email_body'],
                                 to=[data['to_email']])

            Response = email.send()

            return 200

        except Exception:

            return 500


class TokenServices:

    @staticmethod
    def generateToken(id, username, email, Password):
        try:
            print("flag")
            Token_payload = {
                'user_id': id,
                'username': username,
                'email': email,
                'exp': timezone.now() + timedelta(seconds=settings.JWT_EXPIRATION_TIME)
            }
            access_token = jwt.encode(Token_payload, config(
                'JWT_SECRET_KEY'), algorithm=config('JWT_ALGORITHM'))
            print("access_token", access_token)

            token = {
                "AccessToken": access_token
            }

            return token
        except:
            status = 500
            return status


class OTPServices:

    @staticmethod
    def GenerateOtpNumber():
        try:
            digits = "0123456789"
            otp_variable = ""
            for i in range(6):
                otp_variable += digits[math.floor(random.random() * 10)]
            Data = {
                "status": 200,
                "otp": otp_variable
            }
            return Data
        except:
            Data = {
                "status": 500,
                "Message": "Unexcpected otp generated failed"
            }

            return Data

    @staticmethod
    def SendOtp(otp_variable, request):
        try:
            Message = "Your OTP : "+otp_variable
            url = str(settings.URL)
            my_data = {
                'sender_id': str(settings.SENDER_Id),
                'message': str(Message),
                'language': 'english',
                'route': 'p',
                'numbers': str(request.data.get("mobileNumber"))
            }
            headers = {
                'authorization': str(settings.AUTHENTICATION_ID),
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            response = requests.request("POST",
                                        url,
                                        data=my_data,
                                        headers=headers)
            returned_msg = json.loads(response.text)
            print(returned_msg['message'])
            Data = {
                "status": 200,
                "Message": returned_msg['message']
            }
            return Data
        except:
            Data = {
                "status": 500,
                "Message": "Unexpected OTP Send Error"
            }
            return Data
