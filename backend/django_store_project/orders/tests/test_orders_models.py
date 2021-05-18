from django.contrib.auth import get_user_model
from django.test import TestCase

from orders.models import OrderItem, Order
from store.models import Game, Genre

User = get_user_model()


class Test_Create_Order(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Genre')
        self.user = User.objects.create_user(email='user@user.com', username='user', password='password')
        self.game1 = Game.objects.create(name='Game1', description='description', price=100, genre=self.genre)
        self.game2 = Game.objects.create(name='Game2', description='description', price=200, genre=self.genre)
        self.item1 = OrderItem.objects.create(game=self.game1, user=self.user)
        self.item2 = OrderItem.objects.create(game=self.game2, qty=3, user=self.user)
        self.genre.save()
        self.user.save()
        self.game1.save()
        self.game2.save()
        self.item1.save()
        self.item2.save()

    def test_create_order_item(self):
        # default quantity 1
        self.assertEqual(self.item1.qty, 1)
        self.assertEqual(self.item1.game.price, 100)
        self.assertEqual(self.item1.game.name, 'Game1')
        self.assertEqual(str(self.item1), '1 of Game1')
        self.assertEqual(self.item2.game.genre.name, 'Genre')
        self.assertEqual(str(self.item2), '3 of Game2')
        # test get_total_item_price method
        self.assertEqual(self.item1.get_total_item_price(), 100)
        self.assertEqual(self.item2.get_total_item_price(), 600)

    def test_create_order(self):
        self.order = Order.objects.create(user=self.user)
        self.order.items.add(self.item1, self.item2)
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.items.all()[0], self.item1)
        self.assertEqual(self.order.items.all()[0].qty, 1)
        self.assertEqual(self.order.items.all()[1].game.name, 'Game2')
        self.assertEqual(self.order.items.all()[1].qty, 3)
        self.assertEqual(str(self.order), str(self.user))
        # test get_total method
        self.assertEqual(self.order.get_total(), 700)
