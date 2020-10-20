from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'transaction_id')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
