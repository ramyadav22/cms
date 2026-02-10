from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Order, OrderItem
from .serializers import OrderSerializer
from menu.models import Menu


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(users=self.request.user)

    def create(self, request, *args, **kwargs):
        items_data = request.data.get('items', [])

        if not items_data:
            return Response(
                {"error": "Items list is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order = Order.objects.create(
            users=request.user,
            status='PENDING'
        )

        total_amount = 0

        for item in items_data:
            menu_id = item.get('menu_item')
            quantity = item.get('quantity', 1)

            if not menu_id:
                return Response(
                    {"error": "menu_item is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            menu = get_object_or_404(Menu, id=menu_id)

            price = menu.price * quantity

            OrderItem.objects.create(
                order=order,
                menu_item=menu,
                quantity=quantity,
                price=price
            )

            total_amount += price

        order.total_amount = total_amount
        order.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
