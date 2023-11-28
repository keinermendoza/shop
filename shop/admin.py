from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('slug', )
    list_display = ["name", "slug"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('slug', )
    list_display = ['name','slug', 'available', 'price', 'created', 'updated']
    list_editable = ['price', 'available']
    # list_filter = ['available', 'created', 'updated']