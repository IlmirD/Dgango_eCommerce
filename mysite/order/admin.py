from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','complete', 'customer', 'total')
    list_filter = ('complete',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
