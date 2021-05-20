from django.contrib import admin

from orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'ref_code', 'ordered', 'ordered_at', 'get_items', 'get_total']
    list_filter = ['created_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['game', 'qty', 'get_total_item_price', 'order', 'get_user']
