from django.db import models
from django.contrib.auth import get_user_model
from store.models import Game
import uuid

User = get_user_model()


class Order(models.Model):
    ref_code = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_at = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at', 'user']

    def __str__(self):
        return f'{self.ref_code}'

    def get_items(self):
        return OrderItem.objects.filter(order=self)

    def get_total(self):
        total = 0
        for order_item in self.get_items():
            total += order_item.get_total_item_price()
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.qty} of {self.game.name}'

    def get_user(self):
        return self.order.user

    def get_total_item_price(self):
        return self.qty * self.game.price
