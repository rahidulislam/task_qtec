from django.contrib import admin
from .models import Brand, Product, Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name', 'slug']
    prepopulated_fields={'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=['id','name', 'slug']
    prepopulated_fields={'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name', 'slug']
    prepopulated_fields={'slug': ('name',)}