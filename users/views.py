from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics,permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerailizer


class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  


class UserListView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAdminUser]
  
class UserProfileView(generics.RetrieveAPIView):
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  
  def get_object(self):
    return self.request.user
  
class RegisterView(generics.CreateAPIView):
  serializer_class = RegisterSerailizer
  permission_classes = [permissions.AllowAny]
  
  

