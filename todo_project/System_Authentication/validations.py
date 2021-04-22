import re

Email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
Mobile_regrex = re.compile("(0/91)?[7-9][0-9]{9}")


def check(email):
    if(re.search(Email_regex, email)):
        return False
    return True


def Parameter_Validation_Checker(attribute, attribute_value, request):
    if attribute is None or attribute == "":
        Message = attribute_value + " Is Required"
        data = {
            "Message": Message,
            "data": request.data
        }
        return data

    return False


def MobileId_Validation_Checker(attribute, request):
    if not Mobile_regrex.match(attribute):
        Message = "Mobile Number Not Valid"
        data = {
            "Message": Message,
            "data": request.data
        }
        return data
    return False


def Otp_Validation_Checker(attribute, request):
    final_value = 999999
    if int(attribute) > final_value:
        Message = "Otp Not Valid"
        data = {
            "Message : ": Message,
            "data : ": request.data
        }
        print("data")
        return data
    print("False")
    return False


def SignUpView_Validation(request):

    username = request.data.get("username")
    Response = Parameter_Validation_Checker(username, "username", request)
    if Response:
        return Response

    email = request.data.get("email")
    Response = Parameter_Validation_Checker(email, "email", request)
    if Response:
        return Response

    Response = check(str(email))
    if Response:
        Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
        data = {
            "Message": Message,
            "data": request.data
        }
        return data

    password = request.data.get("password")
    Response = Parameter_Validation_Checker(password, "password", request)
    if Response:
        return Response

    confirm_password = request.data.get("confirm_password")
    Response = Parameter_Validation_Checker(
        confirm_password, "confirm_password", request)
    if Response:
        return Response

    role = request.data.get("role")
    Response = Parameter_Validation_Checker(
        role, "role", request)
    if Response:
        return Response

    return False


def SendEmailView_Validation(request):
    email = request.data.get("email")
    Response = Parameter_Validation_Checker(email, "email", request)
    if Response:
        return Response
    return False


def LoginEmailview_Validation(request):
    email = request.data.get("email")
    Response = Parameter_Validation_Checker(email, "email", request)
    if Response:
        return Response

    Response = check(str(email))
    if Response:
        Message = "Invalid Email Id. Example : vishalpwaman@gmail.com"
        data = {
            "Message": Message,
            "data": request.data
        }
        return data

    password = request.data.get("password")
    Response = Parameter_Validation_Checker(password, "password", request)
    if Response:
        return Response


def MobileId_Validation(request):
    mobileNumber = request.data.get("mobileNumber")
    Response = Parameter_Validation_Checker(
        mobileNumber, "mobileNumber", request)
    if Response:
        return Response

    Response = MobileId_Validation_Checker(
        mobileNumber, "mobileNumber", request)
    if Response:
        return Response

    return False


def OtpVerificationValidation(request):
    mobileNumber = request.data.get("mobileNumber")
    Response = Parameter_Validation_Checker(
        mobileNumber, "mobileNumber", request)
    if Response:
        return Response

    Response = MobileId_Validation_Checker(
        mobileNumber, request)
    if Response:
        return Response

    Otp = request.data.get("otp")
    print("Otp :", Otp)
    Response = Otp_Validation_Checker(Otp, request)
    print("Response :", Response)
    if Response:
        return Response

    return False
