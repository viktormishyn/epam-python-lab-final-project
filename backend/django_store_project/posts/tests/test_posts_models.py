from django.contrib.auth import get_user_model
from django.test import TestCase

from store.models import Game, Genre
from posts.models import Post, PostReply

User = get_user_model()


class Test_Create_Post(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Genre')
        self.game = Game.objects.create(name='Game', description='description', price=100, genre=self.genre)

        self.user1 = User.objects.create_user(email='user1@user.com', username='user1', password='password')
        self.user2 = User.objects.create_user(email='user2@user.com', username='user2', password='password')

        self.post = Post.objects.create(game=self.game, author=self.user1, content='Post content')
        self.reply1 = PostReply.objects.create(post=self.post, author=self.user2, content='First reply content')
        self.reply2 = PostReply.objects.create(post=self.post, author=self.user1, content='Second reply content')
        self.genre.save()
        self.game.save()
        self.user1.save()
        self.user2.save()
        self.post.save()
        self.reply1.save()
        self.reply2.save()

    def test_create_post_and_replies(self):
        self.assertEqual(self.post.game, self.game)
        self.assertEqual(self.post.author, self.user1)
        self.assertEqual(self.post.content, 'Post content')

        self.assertEqual(len(Post.objects.all().filter(game=1)), 1)
        self.assertEqual(len(PostReply.objects.all().filter(post=1)), 2)

        self.assertEqual(self.reply1.author, self.user2)
        self.assertEqual(self.reply1.content, 'First reply content')
        self.assertEqual(self.reply1.post.game, self.game)

        self.assertEqual(self.reply2.author, self.user1)
        self.assertEqual(self.reply2.content, 'Second reply content')
        self.assertEqual(self.reply2.post.game.name, 'Game')

        self.assertEqual(str(self.post), 'Post 1')
        self.assertEqual(str(self.reply1), 'PostReply 1')
        self.assertEqual(str(self.reply2), 'PostReply 2')
