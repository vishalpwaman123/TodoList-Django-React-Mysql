from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name="apiOverview"),
    path('taskList/', views.productalllist, name="productalllist"),
    path('productonelist/<int:pk>/', views.productonelist, name="productonelist"),
    path('CreateProduct/', views.CreateProduct, name="Create-Product"),
    path('UpdateProduct/<int:pk>/', views.UpdateProduct, name="Update-Product"),
    path('DeleteProduct/<int:pk>/', views.DeleteProduct, name="Delete-Product")
]
