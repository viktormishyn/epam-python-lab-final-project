from rest_framework import serializers

from .models import Order, OrderItem
from store.serializers import GameSerializer
from users.serializers import OrderUserSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    game = GameSerializer(read_only=True, many=False)

    class Meta:
        model = OrderItem
        fields = ('game', 'qty')


class OrderSerializer(serializers.ModelSerializer):

    Order_id = OrderUserSerializer(read_only=True, many=False)
    items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('Order_id', 'created_at', 'items')
