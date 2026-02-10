from django.urls import path
from .views import AddToCartView,CartView,RemoveFromCartView,UpdateFromCartView


urlpatterns = [
    path('',CartView.as_view(),name = 'view-cart'),
    path('add/',AddToCartView.as_view(),name = "add-to-cart"),
    path('remove/<int:item_id>',RemoveFromCartView.as_view(),name = "remove-cart-item"),
    path('quantity/<int:item_id>/',UpdateFromCartView.as_view(),name = "update-quantity")
]
