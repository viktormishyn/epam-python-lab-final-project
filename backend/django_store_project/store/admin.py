from django.contrib import admin
from store.models import Game, Genre


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'genre']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
