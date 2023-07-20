""" Shop Admin Area Settings """
from django.contrib import admin
from .models import Product, Category, SubCategory


class ProductAdmin(admin.ModelAdmin):
    """ Display fields for Products in Admin """
    list_display = (
        'name',
        'sku',
        'price',
        'description',
        'image',
        'likes',
        'category',
        'subcategory',
        'digital_artwork',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """ Display fields for Categories in Admin """
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    """ Display fields for Subcategories in Admin """
    list_display = (
        'friendly_name',
        'name',
        'category',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
