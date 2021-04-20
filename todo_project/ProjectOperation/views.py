from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializations import *
from .models import product
from .validations import *


class productalllistView(GenericAPIView):

    def get(self, request):
        try:
            try:
                products = product.objects.all()
            except product.DoesNotExist:
                return Response("Database Empty", status=status.HTTP_404_NOT_FOUND)
            serializer = ProductAllDataSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            Message = "Internel Server Error (Exception)"
            return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class productonelistView(GenericAPIView):
    id_param_config = openapi.Parameter(
        'id', in_=openapi.IN_QUERY, description='User Id', type=openapi.TYPE_INTEGER) \


    @swagger_auto_schema(manual_parameters=[id_param_config])
    def get(self, request):
        pk = request.GET.get('id')
        try:
            print(pk)
            try:
                products = product.objects.get(id=pk)
                print(products)
            except product.DoesNotExist:
                return Response("Invalid User Id", status=status.HTTP_404_NOT_FOUND)
            serializer = ProductAllDataSerializer(products, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            Message = "Internel Server Error (Exception)"
            return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateProductView(GenericAPIView):

    serializer_class = CreateProductSerializer

    def post(self, request):
        try:
            # print(request.data)
            Validation_Response = CreateProductView_Validation(request)
            if Validation_Response:
                return Response(Validation_Response, status=status.HTTP_400_BAD_REQUEST)

            serializer = CreateProductSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                data = "Create Operation Failed"
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            Message = "Internel Server Error (Exception)"
            return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateProductView(GenericAPIView):

    serializer_class = UpdateProductSerializer

    def patch(self, request):
        try:
            user_id = request.GET.get('id')
            try:
                products = product.objects.get(id=user_id)
                # print(products)
            except product.DoesNotExist:
                return Response("Invalid User Id", status=status.HTTP_404_NOT_FOUND)

            serializer = ProductAllDataSerializer(
                instance=products, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                data = 'Update Operation Failed'
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            Message = "Internel Server Error (Exception)"
            return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteProductView(GenericAPIView):

    id_param_config = openapi.Parameter(
        'id', in_=openapi.IN_QUERY, description='User Id', type=openapi.TYPE_INTEGER) \


    @swagger_auto_schema(manual_parameters=[id_param_config])
    def delete(self, request):
        pk = request.GET.get('id')
        try:
            try:
                products = product.objects.get(id=pk)
            except product.DoesNotExist:
                return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)

            products.delete()
            data = "Item Successfully Deleted"
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            Message = "Internel Server Error (Exception)"
            return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
