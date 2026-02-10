from django.db import models
from django.conf import settings
from menu.models import Menu
class Order(models.Model):
  STATUS_CHOICES = (
    ('PENDING','pending'),
    ('preparing','Preparing'),
    ('completed','Completed'),
    ('cancelled','Cancelled')
  )
  
  
  ORDER_TYPE = (
    ('DINE_IN','Dine In'),
    ('TAKEAWAY','Takeaway')
  )
  
  
  users = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null= True,
    related_name='orders'
  )
  
  
  
  status = models.CharField(max_length=20,
                            choices=STATUS_CHOICES,
                            default='pending')
  
  
  total_amount  = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      default=0.00)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    db_table = 'orders'
    ordering = ['created_at']
    
  def __str__(self):
    return f'Order #{self.id}'
  
class OrderItem(models.Model):
  order = models.ForeignKey(
    Order,
    on_delete = models.CASCADE,
    related_name = 'items'
  )
  menu_item = models.ForeignKey(
    Menu,
    on_delete=models.CASCADE
    
    
  )
  
  quantity = models.PositiveIntegerField(default=1)
  
  price = models.DecimalField(max_digits=8, decimal_places=2)
  
  class Meta:
    db_table = 'order_item'
    
  def __str__(self):
    return f"{self.menu_item.name} x {self.quantity}"