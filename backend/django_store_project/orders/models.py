from django.db import models
from django.contrib.auth import get_user_model
from store.models import Game

User = get_user_model()


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.qty} of {self.game.name}'

    def get_total_item_price(self):
        return self.qty * self.game.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    created_at = models.DateTimeField(auto_now_add=True)
    # ordered_at = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at', 'user']

    def __str__(self):
        return f'{self.user}'

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
