from rest_framework import serializers

from .models import Order, OrderInfo, OrderItem
from store.serializers import GameOrderSerializer


class OrderInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderInfo
        fields = ('order', 'first_name', 'last_name', 'email', 'phone', 'payment_type', 'comments')


class OrderItemSerializer(serializers.ModelSerializer):

    game = GameOrderSerializer(read_only=True, many=False)

    class Meta:
        model = OrderItem
        fields = ('game', 'qty', 'order')


class OrderSerializer(serializers.ModelSerializer):

    get_items = OrderItemSerializer(many=True)
    order_info = OrderInfoSerializer(many=False)

    class Meta:
        model = Order
        fields = ('ref_code', 'user', 'created_at', 'ordered', 'ordered_at', 'get_items', 'get_total', 'order_info')
