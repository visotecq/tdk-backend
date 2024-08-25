from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer,CategorySerializer,ServiceSerializer
from .models import Product,Category,Service

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()