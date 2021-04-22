from django.urls import path, include
from .views import *

urlpatterns = [
    path('Signup/', SignUp_View.as_view(), name="SignUp"),
    path('SendVerificationEmail/', SendEmailView.as_view(),
         name="Send Verification Email"),
    path('VerifyEmail/', VerifyEmailView.as_view(), name="Verify Email View"),
    path('LoginApi/', LoginApiView.as_view(), name="Verify Email View"),
    path('GenerateOtpApi/', GenerateOtpApiView.as_view(),
         name="Generate Otp"),
    path('OtpVerification/', OtpVerificationView.as_view(),
         name="Otp Verification"),
]
