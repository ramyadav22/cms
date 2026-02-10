
from rest_framework import serializers
from .models import Menu

class MenuSerailizer(serializers.ModelSerializer):
  class Meta:
    model=Menu
    fields = '__all__'
    
    
  