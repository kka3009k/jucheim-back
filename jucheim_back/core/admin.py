from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class PhotoProductsAdmin(admin.TabularInline):
    model = PhotoProducts

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [PhotoProductsAdmin]

@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ('id','category','product','photo_banner')
 