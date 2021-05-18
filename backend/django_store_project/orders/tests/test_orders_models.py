from django.contrib.auth import get_user_model
from django.test import TestCase

from orders.models import CartItem, Cart
from store.models import Game, Genre

User = get_user_model()


class Test_Create_Cart(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Genre')
        self.user = User.objects.create_user(email='user@user.com', username='user', password='password')
        self.game1 = Game.objects.create(name='Game1', description='description', price='100', genre=self.genre)
        self.game2 = Game.objects.create(name='Game2', description='description', price='200', genre=self.genre)
        self.item1 = CartItem.objects.create(game=self.game1)
        self.item2 = CartItem.objects.create(game=self.game2, quantity=3)
        self.genre.save()
        self.user.save()
        self.game1.save()
        self.game2.save()
        self.item1.save()
        self.item2.save()

    def test_create_cart_item(self):
        # default quantity 1
        self.assertEqual(self.item1.quantity, 1)
        self.assertEqual(self.item1.game.name, 'Game1')
        self.assertEqual(str(self.item1), 'Game1')
        self.assertEqual(self.item2.game.genre.name, 'Genre')
        self.assertEqual(str(self.item2), 'Game2')

    def test_create_cart(self):
        self.cart = Cart.objects.create(cart_id=self.user)
        self.cart.items.add(self.item1, self.item2)
        self.assertEqual(self.cart.cart_id, self.user)
        self.assertEqual(self.cart.items.all()[0], self.item1)
        self.assertEqual(self.cart.items.all()[0].quantity, 1)
        self.assertEqual(self.cart.items.all()[1].game.name, 'Game2')
        self.assertEqual(self.cart.items.all()[1].quantity, 3)
        self.assertEqual(str(self.cart), str(self.user))
