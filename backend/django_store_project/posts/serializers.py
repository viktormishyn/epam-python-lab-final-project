from rest_framework import serializers

from .models import Post, PostReply
from users.serializers import UserPostSerializer


class PostReplySerializer(serializers.ModelSerializer):

    author = UserPostSerializer(read_only=True, many=False)

    class Meta:
        model = PostReply
        fields = ('id', 'post', 'author', 'created_at', 'content', 'edited')


class PostSerializer(serializers.ModelSerializer):

    author = UserPostSerializer(read_only=True, many=False)
    get_replies = PostReplySerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'game', 'author', 'created_at', 'content', 'edited', 'get_replies')
