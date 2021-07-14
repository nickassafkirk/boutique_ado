from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    #  list_display is a tuple which tells admin which fields to display
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )

    ordering = ('sku',)
    # This sorts thwee fields by sku, to reverse sort add a - before the sku
    # This needs to be a tuple because we can sort by multiple fields


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
