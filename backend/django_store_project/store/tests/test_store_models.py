from django.contrib.auth import get_user_model
from django.test import TestCase

from store.models import Game, Genre

User = get_user_model()


class Test_Create_Game(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Genre')
        self.user = User.objects.create_user(email='user@user.com', username='user', password='password')
        self.game = Game.objects.create(name='Game', description='description', price='100', genre=self.genre)

    def test_store_content(self):
        game = Game.objects.get(id=1)
        name = f'{game.name}'
        description = f'{game.description}'
        price = f'{game.price}'
        genre = f'{game.genre}'

        self.assertEqual(name, 'Game')
        self.assertEqual(description, 'description')
        self.assertEqual(price, '100.00')
        self.assertEqual(genre, 'Genre')

        self.assertEqual(str(game), 'Game')
