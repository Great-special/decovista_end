from django.contrib import admin
from .models import Products, Category, Review

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['designer__username','product_name', 'category__category_name', 'brand', 'price']
    list_filter = ['product_name',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name',]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product__product_name', 'rating', 'comment']
    