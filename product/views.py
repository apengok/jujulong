from django.shortcuts import render

# Create your views here.
from .models import  Category, Brand,Color,Size,Goods
from rest_framework import viewsets
from .serializers import CategorySerializer, BrandSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer