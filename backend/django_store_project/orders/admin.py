from django.contrib import admin

from orders.models import Order, OrderItem, OrderInfo


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'ref_code', 'ordered', 'ordered_at', 'get_items', 'get_total', 'order_info']
    list_filter = ['created_at']


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['order', 'first_name', 'last_name', 'email', 'phone', 'payment_type', 'comments']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['game', 'qty', 'get_total_item_price', 'order', 'get_user']
