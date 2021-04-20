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
from datetime import datetime, timedelta
from django.utils import timezone
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
