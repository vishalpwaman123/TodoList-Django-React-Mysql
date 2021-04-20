from django.db import models
import datetime
# Create your models here.


class UserAccoutDetail(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=500, blank=False, null=False)
    # confirm_password = models.CharField(
    #     max_length=500, blank=False, null=False, default=False)
    role = models.TextField()
    mobileNumber = models.DecimalField(
        max_digits=10, decimal_places=0, default=True)
    user_dateOfBirth = models.CharField(max_length=50, default=True)
    gender = models.CharField(max_length=10, null=True)
    is_verified = models.BooleanField(default=False)
    is_actived = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
