from django.db import models
from django.contrib.auth import get_user_model

from store.models import Game

User = get_user_model()


class OrderItem(models.Model):
    game = models.OneToOneField(Game, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.game.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    # payment_details = models.ForeignKey(Payment, null=True)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.game.price for item in self.items.all()])

    def __str__(self):
        return f'{self.user} - {self.ref_code}'
