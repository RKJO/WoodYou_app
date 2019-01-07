from django.contrib import admin

from .models import Product, Material

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_lm', 'price_m2', 'category_name')
    ordering = ('id',)
    list_display_links = ('id', 'name')
    list_filter = ('category_name',)
    list_editable = ('price_lm', 'price_m2')
    search_fields = ('name', 'category_name')
    list_per_page = 25

admin.site.register(Product, ProductAdmin)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category_name')
    ordering = ('id',)
    list_display_links = ('id', 'name')
    list_filter = ('category_name',)
    list_editable = ('price',)
    search_fields = ('name', 'category_name')
    list_per_page = 25

admin.site.register(Material, MaterialAdmin)