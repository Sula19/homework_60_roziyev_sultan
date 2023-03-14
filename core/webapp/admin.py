from django.contrib import admin
from webapp.models import Product, Basket, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'remainder', 'category', 'created')
    list_filter = ('id', 'category', 'created')
    search_fields = ('name', 'category')
    fields = ('name', 'description', 'img', 'price', 'remainder', 'category', 'created')
    readonly_fields = ('id', 'created')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'qty')
    list_filter = ('id', 'product')
    search_fields = ('product',)
    fields = ('product', 'qty')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address', 'created')
    list_filter = ('id', 'product', 'user', 'phone', 'address', 'created')
    search_fields = ('user', 'phone', 'address')
    fields = ('user', 'phone', 'address', 'created')
    readonly_fields = ('id', 'created')


admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)
