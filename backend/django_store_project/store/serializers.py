from rest_framework import serializers

from .models import Game, Genre

from posts.serializers import PostSerializer


class GameSerializer(serializers.ModelSerializer):

    get_posts = PostSerializer(many=True, required=False)

    class Meta:
        model = Game
        fields = ('id', 'name', 'slug', 'genre', 'description', 'price',
                  'image', 'get_thumbnail', 'get_posts')


class GameOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'genre', 'price', 'get_thumbnail')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
