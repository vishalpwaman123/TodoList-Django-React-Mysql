from django.db import models
from datetime import datetime
# Create your models here.


class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    # updated_at = models.DateTimeField(auto_now=True, default=datetime.now)

    def __str__(self):
        return self.name

    # class Meta:
    #     abstract = True


class Userdata(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=100, null=False,
                             blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    account = models.CharField(max_length=200, null=False, blank=False)
    mobileNumber = models.CharField(max_length=15, null=False, blank=False)
    dateOfBirth = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=6, null=False, blank=False)
    # created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    # updated_at = models.DateTimeField(auto_now=True, default=datetime.now)

    def __str__(self):
        return self.email

    # class Meta:  # Use for auto datetime creation
    #     abstract = True
