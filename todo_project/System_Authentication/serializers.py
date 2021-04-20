from rest_framework import serializers
from .models import UserAccoutDetail


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=500)
    confirm_password = serializers.CharField(max_length=500)
    role = serializers.CharField(max_length=20)
    mobileNumber = serializers.DecimalField(
        max_digits=10, decimal_places=0)
    user_dateOfBirth = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=10)

    class Meta:
        model = UserAccoutDetail
        fields = ['username', 'email', 'password',
                  'confirm_password', 'role', 'mobileNumber', 'user_dateOfBirth', 'gender']
        # fields = '__all__'


class SignUpFinalSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=500)
    role = serializers.CharField(max_length=20)
    mobileNumber = serializers.DecimalField(
        max_digits=10, decimal_places=0)
    user_dateOfBirth = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=10)

    class Meta:
        model = UserAccoutDetail
        fields = ['username', 'email', 'password',
                  'role', 'mobileNumber', 'user_dateOfBirth', 'gender']


class EmailResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccoutDetail
        fields = ['email']


class EmailAccountVarificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccoutDetail
        fields = ['id', 'username',
                  'email', 'password', 'is_verified']


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccoutDetail
        fields = ['email', 'password']


class FetchUserAllData(serializers.ModelSerializer):
    class Meta:
        model = UserAccoutDetail
        fields = ['username', 'email', 'role',
                  'mobileNumber', 'user_dateOfBirth', 'gender', 'is_verified', 'is_actived', 'created_at']
 