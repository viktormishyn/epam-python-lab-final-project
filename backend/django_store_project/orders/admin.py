from django.contrib import admin

from orders.models import Order, OrderItem


@admin.register(Order)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    list_filter = ['created_at']


@admin.register(OrderItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['game', 'qty']
