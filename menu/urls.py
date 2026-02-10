from django.urls import path
from .views import MenuViewSet

urlpatterns = [
    path('menu-items/', MenuViewSet.as_view(), name = "menu-items")
]
