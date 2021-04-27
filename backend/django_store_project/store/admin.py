from django.contrib import admin
from store.models import Game


@admin.register(Game)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'genre']
