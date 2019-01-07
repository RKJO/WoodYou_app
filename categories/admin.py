from django.contrib import admin
from .models import ProductCategory, MaterialCategory, RealizationCategory

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
    list_display_links = ('id',)
    list_filter = ('id', 'name')
    list_editable = ('name',)
    list_per_page = 25

admin.site.register(ProductCategory, ProductCategoryAdmin)

class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
    list_display_links = ('id',)
    list_filter = ('id', 'name')
    list_editable = ('name',)
    list_per_page = 25

admin.site.register(MaterialCategory, MaterialCategoryAdmin)

class RealizationCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
    list_display_links = ('id',)
    list_filter = ('id', 'name')
    list_editable = ('name',)
    list_per_page = 25

admin.site.register(RealizationCategory, RealizationCategoryAdmin)