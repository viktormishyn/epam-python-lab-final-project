from rest_framework import serializers

from .models import Game, Genre


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'slug', 'genre', 'description', 'price',
                  'image', 'get_thumbnail')


class GameOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'genre', 'price', 'get_thumbnail')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
