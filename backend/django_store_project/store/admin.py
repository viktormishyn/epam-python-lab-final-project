from django.contrib import admin
from django.utils.safestring import mark_safe

from store.models import Game, Genre


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['image_show', 'name', 'price', 'genre', 'added']
    list_filter = ['genre', 'added']
    list_editable = ['price', 'genre']

    def image_show(self, obj):
        if obj.thumbnail:
            return mark_safe(f"<img src='{obj.thumbnail.url}' width='60'/>")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
