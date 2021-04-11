from rest_framework import serializers
from .models import product, Userdata

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class userdataSerializeer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = '__all__'
