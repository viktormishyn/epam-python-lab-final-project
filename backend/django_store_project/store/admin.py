from django.contrib import admin

from store.models import Game, Genre


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'genre', 'added']
    list_filter = ['genre', 'added']
    list_editable = ['price', 'genre']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
