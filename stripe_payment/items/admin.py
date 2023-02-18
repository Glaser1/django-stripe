from django.contrib import admin
from items.models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    search_fields = ('name', 'description', 'price')
    empty_value_display = '-пусто-'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created')
    search_fields = ('created',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)

