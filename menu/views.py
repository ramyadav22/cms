from django.shortcuts import render

from .models import Menu
from .seralizers import MenuSerailizer
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView




class MenuViewSet(ListAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerailizer
  permission_classes = [AllowAny]
  
  


