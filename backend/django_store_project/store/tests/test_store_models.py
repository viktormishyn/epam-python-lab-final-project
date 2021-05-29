from django.contrib.auth import get_user_model
from django.test import TestCase

from store.models import Game, Genre
from posts.models import Post, PostReply

from django.db.utils import IntegrityError

User = get_user_model()


class Test_Create_Game(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Genre')
        self.user1 = User.objects.create_user(email='user1@user.com', username='user1', password='password')
        self.user2 = User.objects.create_user(email='user2@user.com', username='user2', password='password')
        self.game1 = Game.objects.create(name='Game1', description='description1', price='100', genre=self.genre)
        self.game2 = Game.objects.create(name='Game2', description='description2', price='200', genre=self.genre)
        self.post = Post.objects.create(game=self.game1, author=self.user1, content='Post content')
        self.reply1 = PostReply.objects.create(post=self.post, author=self.user2, content='First reply content')
        self.reply2 = PostReply.objects.create(post=self.post, author=self.user1, content='Second reply content')
        self.genre.save()
        self.game1.save()
        self.game2.save()
        self.user1.save()
        self.user2.save()
        self.post.save()
        self.reply1.save()
        self.reply2.save()

    def test_store_content(self):
        game = Game.objects.get(id=1)
        name = f'{game.name}'
        description = f'{game.description}'
        price = f'{game.price}'
        genre = f'{game.genre}'

        self.assertEqual(name, 'Game1')
        self.assertEqual(description, 'description1')
        self.assertEqual(price, '100.00')
        self.assertEqual(genre, 'Genre')

        self.assertEqual(str(game), 'Game1')

    def test_game_should_not_cost_less_than_zero(self):
        with self.assertRaises(IntegrityError):
            Game.objects.create(name='Game_negative_price',
                                description='description', price='-1', genre=self.genre)

    def test_game_can_cost_zero(self):
        game_zero = Game.objects.create(name='Game_negative_price',
                                        description='description', price='0', genre=self.genre)
        price = f'{game_zero.price}'
        self.assertEqual(game_zero.price, '0')

    def test_game_posts_and_replies(self):
        self.assertEqual(len(self.game1.get_posts()), 1)
        self.assertEqual(len(self.game2.get_posts()), 0)
        self.assertEqual(len(self.game1.get_posts()[0].get_replies()), 2)
