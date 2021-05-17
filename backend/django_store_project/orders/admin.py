from django.contrib import admin

from orders.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'created_at']
    list_filter = ['created_at']
