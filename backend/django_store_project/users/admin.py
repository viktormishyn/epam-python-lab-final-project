from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import CharField, Textarea, TextInput

from users.models import User


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username')
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'id', 'username', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)
