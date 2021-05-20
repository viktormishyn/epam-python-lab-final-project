from rest_framework import serializers

from .models import Order, OrderItem
from store.serializers import GameOrderSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    game = GameOrderSerializer(read_only=True, many=False)

    class Meta:
        model = OrderItem
        fields = ('game', 'qty', 'order')


class OrderSerializer(serializers.ModelSerializer):

    get_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('ref_code', 'user', 'created_at', 'ordered', 'ordered_at', 'get_items', 'get_total')
