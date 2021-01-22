from django.contrib import admin
from .models import Product, Discount, Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'disc_price', 'description', 'image']
    readonly_fields = ['disc_price']


class AdminDiscount(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'product', 'disc_per']


class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'price', 'mode_of_payment', 'date', 'status']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Discount, AdminDiscount)
admin.site.register(Order, AdminOrder)
