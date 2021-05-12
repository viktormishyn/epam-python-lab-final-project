from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Game, Genre


class Test_Create_Game(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_genre = Genre.objects.create(name="Genre")
        testuser1 = User.objects.create_user(
            username='testuser1', password='12345678')
        test_game = Game.objects.create(
            name="Game", description="description", price="100", genre=test_genre)

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
