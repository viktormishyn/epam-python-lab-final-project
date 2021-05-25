from django.db import models
from django.contrib.auth import get_user_model
from store.models import Game

User = get_user_model()


class Post(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Post {self.id}'


class PostReply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'PostReply {self.id}'
