from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from django.db.models.signals import pre_save, post_save

from .models import Order, OrderItem
from store.models import Game
from .permissions import isAdminOrReadOnly  # TODO
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import OrderItemSerializer, OrderSerializer

from rest_framework.response import Response


# class ListOrder(generics.ListCreateAPIView):
#     permission_classes = (IsAdminUser,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAdminUser,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# def add_to_cart(request, id):
#     game = get_object_or_404(Game, id=id)
#     order = Order.objects.filter(user=request.user, is_ordered=False)
#     if order.exists():
#         # check if the order item is in the order
#         if order.items.filter()

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(user=request.user, ordered=False).first()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        user = request.user
        order, _ = Order.objects.get_or_create(user=user, ordered=False)
        game = Game.objects.get(id=data.get('id'))
        qty = data.get('qty')
        order_item = OrderItem(game=game, qty=qty, order=order)
        order_item.save()
        return Response({'success': 'item is added to order'}, status=status.HTTP_200_OK)

    def update(self, request):
        pass

    def delete(self, request):
        pass


# @receiver(pre_save, sender=OrderItem)
# def correct_price(sender, **kwargs):
#     print('I got called')
