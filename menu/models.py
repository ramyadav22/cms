from django.db import models

class Menu(models.Model):
  CATEGORY_CHOICES = (
    ('coffee','Coffee'),
    ('snacks','Snacks'),
    ('dessert','Dessert'),
    ('meal','Meal')
  )
  
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  description = models.TextField(blank=True,null=True)
  image = models.URLField(blank=True, null=True) 
  is_available = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  
  
  class Meta:
    db_table = 'menu'
    ordering = ['name']
    
    
  def __str__(self):
    return self.name
