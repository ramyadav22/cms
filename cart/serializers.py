from rest_framework import serializers
from .models import CartItemModel,Cart

class CartItemSerializer(serializers.ModelSerializer):
  menu_name = serializers.CharField(source = 'menu_item.name', read_only = True)
  price = serializers.DecimalField(source = 'menu_item.price', max_digits=8,decimal_places=2,read_only = True)
  
  class Meta:
    model = CartItemModel
    fields = ['id','menu_item','menu_name', 'price','quantity']
    

class CartSerailizer(serializers.ModelSerializer):
  items = CartItemSerializer(many = True, read_only = True)
  
  class Meta:
    model = Cart
    fields = ['id','items']
  