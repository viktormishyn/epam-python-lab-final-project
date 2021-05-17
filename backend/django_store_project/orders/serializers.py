from rest_framework import serializers

from .models import Cart
from store.serializers import GameSerializer
from users.serializers import CartUserSerializer


class CartSerializer(serializers.ModelSerializer):

    cart_id = CartUserSerializer(read_only=True, many=False)
    games = GameSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'games')
