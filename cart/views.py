from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cart,CartItemModel
from menu.models import Menu
from .serializers import CartSerailizer


class AddToCartView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    menu_id = request.data.get('menu_item')
    quantity = int(request.data.get('quantity', 1))

    cart, _ = Cart.objects.get_or_create(user=request.user)

    menu = get_object_or_404(Menu, id=menu_id)

    cart_item, created = CartItemModel.objects.get_or_create(
        cart=cart,
        menu_item=menu
    )

    if created:
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity

    cart_item.save()

    return Response(
        {"message": "Item added to cart"},
        status=status.HTTP_200_OK
    )




class CartView(APIView):
  permission_classes = [IsAuthenticated]
  
  
  def get(self,request):
    cart,_ = Cart.objects.get_or_create(user = request.user)
    serializer = CartSerailizer(cart)
    return Response(serializer.data)



class RemoveFromCartView(APIView):
  permission_classes = [IsAuthenticated]
  
  def delete(self,request,item_id):
    cart =Cart.objects.get(user = request.user)
    CartItemModel.objects.filter(cart=cart,id=item_id).delete()
    return Response({"message":"Item removed"}, status=status.HTTP_200_OK)
        


# class UpdateFromCartView(APIView):

#     def patch(self, request, *args, **kwargs):
#         item_id = kwargs.get("item_id")
#         action = request.data.get("action")
        
#         try:
#             cart_item = CartItemModel.objects.get(
#                 id=item_id,
               
#             )
#         except CartItemModel.DoesNotExist:
#             return Response(
#                 {"error": "Item not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         if action == "inc":
#             cart_item.quantity += 1
#         elif action == "dec":
#             if cart_item.quantity > 1:
#                 cart_item.quantity -= 1
                
#             else:
#                 cart_item.delete()
#                 return Response(
#                     {"message": "Item removed"},
#                     status=status.HTTP_204_NO_CONTENT
#                 )
                
#         else:
#             return Response(
#                 {"error": "Invalid action"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         cart_item.save()

#         return Response({
#             "id": cart_item.id,
#             "quantity": cart_item.quantity
#         })


class UpdateFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, item_id):
        action = request.data.get("action")

        try:
            cart_item = CartItemModel.objects.get(
                id=item_id,
                cart__user=request.user
            )
        except CartItemModel.DoesNotExist:
            return Response(
                {"error": "Item not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if action == "inc":
            cart_item.quantity += 1
            cart_item.save()

            return Response({
                "id": cart_item.id,
                "quantity": cart_item.quantity
            })

        elif action == "dec":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()

                return Response({
                    "id": cart_item.id,
                    "quantity": cart_item.quantity
                })
            else:
                cart_item.delete()
                return Response(
                    {"message": "Item removed"},
                    status=status.HTTP_200_OK
                )

        return Response(
            {"error": "Invalid action"},
            status=status.HTTP_400_BAD_REQUEST
        )
