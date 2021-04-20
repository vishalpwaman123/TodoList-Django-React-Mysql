from .models import product
from rest_framework import serializers


class ProductAllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['name', 'category', 'price', 'description', 'stars']


class UpdateProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=500)
    price = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=500)
    stars = serializers.IntegerField()

    class Meta:
        model = product
        fields = ['id', 'name', 'category', 'price', 'description', 'stars']
