from rest_framework.routers import DefaultRouter
from .views import UserViewSet,RegisterView
from django.urls import path



urlpatterns = [
  
  path('', RegisterView.as_view(), name = 'register'),
  
]
