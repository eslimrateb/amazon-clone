from django.contrib import admin

# Register your models here.
from .models import Product, ProductImages, Brand, Review


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'flag', 'sku')
    search_fields = ('name', 'brand__name')
    list_filter = ('flag', 'brand')
    inlines = [ProductImagesInline]
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)