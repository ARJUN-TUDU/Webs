from django.urls import path 
from . import views as views



urlpatterns = [
     path('',views.getRouts,name="routes"),
     path('products/',views.myProducts , name = "products"),
     path('products/<str:pk>',views.myProduct , name = "product"), 
] 