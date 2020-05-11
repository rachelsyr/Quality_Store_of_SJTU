from django.contrib import admin
from .models import ShopType, Shop

# Register your models here.

@admin.register(ShopType)
class ShopTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop_type', 'content')