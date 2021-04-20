from django.urls import path, include
from .views import *

urlpatterns = [
    path('CreateProduct/', CreateProductView.as_view(), name="Create Product"),
    path('productalllist/', productalllistView.as_view(),
         name="product all list"),
    path('productonelist/', productonelistView.as_view(),
         name="product one list"),
    path('UpdateProduct/', UpdateProductView.as_view(), name="Update Product"),
    path('DeleteProduct/', DeleteProductView.as_view(), name="Delete Product"),
]
