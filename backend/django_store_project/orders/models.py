from django.db import models
from django.contrib.auth import get_user_model
from store.models import Game

User = get_user_model()


class CartItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.game.name


class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(CartItem)

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}'
