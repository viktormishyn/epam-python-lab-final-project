from rest_framework import status
from rest_framework.views import APIView
# from django.db.models.signals import pre_save, post_save

from .models import Order, OrderItem, OrderInfo
from store.models import Game
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderItemSerializer, OrderSerializer, OrderInfoSerializer
from django.utils import timezone


from rest_framework.response import Response


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    # get user's cart (unique Order object with ordered=False field)
    def get(self, request):
        order = Order.objects.filter(user=request.user, ordered=False).first()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # add item to user's cart (if cart doesn't exist it will be created)
    def post(self, request):
        data = request.data
        user = request.user
        order, _ = Order.objects.get_or_create(user=user, ordered=False)
        game = Game.objects.get(id=data.get('id'))
        qty = data.get('qty')
        if OrderItem.objects.filter(order=order, game=game).exists():
            return Response({'msg': 'Item already exists'}, status=status.HTTP_409_CONFLICT)
        order_item = OrderItem(game=game, qty=qty, order=order)
        order_item.save()
        return Response({'success': 'Item is added to the order'}, status=status.HTTP_200_OK)

    # change quantity in cart item
    def put(self, request):
        data = request.data
        order = Order.objects.filter(user=request.user, ordered=False).first()
        order_item = OrderItem.objects.filter(order=order, game=data.get('id')).first()
        qty = data.get('qty')
        order_item.qty = qty
        order_item.save()
        return Response({'success': 'Item is updated'}, status=status.HTTP_200_OK)

    # delete cart item by it's id
    def delete(self, request):
        data = request.data
        order = Order.objects.filter(user=request.user, ordered=False).first()
        order_item = OrderItem.objects.filter(order=order, game=data.get('id'))
        order_item.delete()
        return Response({'success': 'Item is deleted from the order'}, status=status.HTTP_204_NO_CONTENT)


class Checkout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order = Order.objects.filter(user=request.user, ordered=False).first()
        data = request.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        comments = data.get('comments')
        payment_type = data.get('payment_type')
        order_info = OrderInfo(order=order, first_name=first_name, last_name=last_name,
                               email=email, phone=phone, payment_type=payment_type, comments=comments)
        order_info.save()
        order.ordered = True
        order.ordered_at = timezone.now()
        order.save()
        return Response({'success': 'The order is ordered'}, status=status.HTTP_200_OK)

# @receiver(pre_save, sender=OrderItem)
# def correct_price(sender, **kwargs):
#     print('I got called')
