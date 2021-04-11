from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import productSerializer, userdataSerializeer
from .models import product, Userdata

# Create your views here.


@api_view(['POST'])
def SignUp(request):
    try:
        serializedata = userdataSerializeer(data=request.data)
        if serializedata.is_valid():
            serializedata.save()
            return Response(serializedata.data, status=status.HTTP_201_CREATED)
    except Exception:
        Message = "Internel Server Error (Exception)"
        return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def SignIn(request):
    try:
        emailId = request.data.get("email")
        passwordId = request.data.get("password")
        print(emailId, passwordId)
        try:
            Userdatas = Userdata.objects.get(
                email=emailId, password=passwordId)
        except Userdata.DoesNotExist:
            return Response("User Not Exist", status=status.HTTP_404_NOT_FOUND)
        print("Flag 1", Userdatas)
        serializedata = userdataSerializeer(Userdatas, many=False)
        print("Flag 2", serializedata.data)
        return Response(serializedata.data, status=status.HTTP_200_OK)

    except Exception:
        Message = "Internel Server Error (Exception)"
        return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def productalllist(request):
    try:
        try:
            products = product.objects.all()
        except product.DoesNotExist:
            return Response("Database Empty", status=status.HTTP_404_NOT_FOUND)
        serializer = productSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception:
        Message = "Internel Server Error (Exception)"
        return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def productonelist(request, pk):
    try:
        print(pk)
        try:
            products = product.objects.get(id=pk)
        except product.DoesNotExist:
            return Response("Database Empty", status=status.HTTP_404_NOT_FOUND)
        serializer = productSerializer(products, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception:
        Message = "Internel Server Error (Exception)"
        return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateProduct(request):
    try:
        # print(request.data)
        serializer = productSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = "Create Operation Failed"
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        Message = "Internel Server Error (Exception)"
        return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def UpdateProduct(request, pk):
    try:
        try:
            products = product.objects.get(id=pk)
        except product.DoesNotExist:
            return Response("Data Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = productSerializer(instance=products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            data = 'Update Operation Failed'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        Message = "Internel Server Error (Exception)"
        return Response(Message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteProduct(request, pk):
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
