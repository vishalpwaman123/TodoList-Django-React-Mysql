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
    class Meta:
        model = product
        fields = ['id', 'name', 'category', 'price', 'description', 'stars']
