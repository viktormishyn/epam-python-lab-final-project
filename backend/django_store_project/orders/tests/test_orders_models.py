from django.contrib.auth import get_user_model
from django.test import TestCase

from django.db.utils import IntegrityError

from orders.models import OrderItem, Order
from store.models import Game, Genre

User = get_user_model()


class Test_Create_Order(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Genre')
        self.user = User.objects.create_user(email='user@user.com', username='user', password='password')
        self.game1 = Game.objects.create(name='Game1', description='description', price=100, genre=self.genre)
        self.game2 = Game.objects.create(name='Game2', description='description', price=200, genre=self.genre)
        self.order = Order.objects.create(user=self.user)
        self.item1 = OrderItem.objects.create(game=self.game1, order=self.order)
        self.item2 = OrderItem.objects.create(game=self.game2, order=self.order, qty=3)
        self.genre.save()
        self.user.save()
        self.game1.save()
        self.game2.save()
        self.order.save()
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
        # test get_user method
        self.assertEqual(self.item1.get_user(), self.user)

    def test_create_order_item_with_negative_quantity(self):
        # game item quantity should not be less than 0
        with self.assertRaises(IntegrityError):
            self.item_negative = OrderItem.objects.create(game=self.game2, order=self.order, qty=-3)

    def test_create_order(self):
        self.assertEqual(self.order.user, self.user)
        # test get_items method
        self.assertEqual(len(self.order.get_items()), 2)
        self.assertEqual(self.order.get_items()[0], self.item1)
        self.assertEqual(self.order.get_items()[0].qty, 1)
        self.assertEqual(self.order.get_items()[1].game.name, 'Game2')
        self.assertEqual(self.order.get_items()[1].qty, 3)
        # test __str__ method
        self.assertEqual(len(str(self.order)), 36)  # valid uuid4 string contains 36 characters
        # test get_total method
        self.assertEqual(self.order.get_total(), 700)
