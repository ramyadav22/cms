from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    
    model = User
    fields = ['username','email','phone','first_name','last_name','is_staff','is_active']
    read_only_fields = ['id','is_staff']
    
    


class RegisterSerailizer(serializers.ModelSerializer):
  password = serializers.CharField(write_only = True)
  class Meta:
    model = User
    fields = ('username','email','password')
    
  def create(self,validated_data):
    user = User.objects.create_user(
      username = validated_data['username'],
      email = validated_data['email'],
      password=validated_data['password']
    )
    
    return user
  