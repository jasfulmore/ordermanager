from django.contrib import admin
from .models import Customer, Product, Order, OrderItem

# Register your models here.

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "order_date")
    inlines = [OrderItemInLine]








admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)