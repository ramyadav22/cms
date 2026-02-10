from django.db import models
from django.conf import settings
from menu.models import Menu

class Cart(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                              on_delete=models.CASCADE,
                              related_name='cart')
  created_at = models.DateTimeField(auto_now_add=True)
  class Meta:
    db_table = 'cart'
  
  def __str__(self):
    return f"Cart -{self.user}"
  

class CartItemModel(models.Model):
  cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
  menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
  quantity = models.PositiveBigIntegerField(default=1)
  class Meta:
    db_table = 'cart_items'
    unique_together = ('cart','menu_item')
  
  def __str__(self):
    return f"{self.menu_item.name} x {self.quantity}"
    
  
