from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post, PostReply


@admin.register(Post)
class GameAdmin(admin.ModelAdmin):
    list_display = ['game', 'author', 'created_at', 'content', 'get_replies']
    list_filter = ['game', 'author', 'created_at']
    list_editable = ['content']


@admin.register(PostReply)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at', 'content']
    list_filter = ['post', 'author', 'created_at']
    list_editable = ['content']
