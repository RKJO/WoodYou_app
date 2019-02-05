from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.views import View
from .models import Product, Material, ProductCategory, MaterialCategory

# Create your views here.

class MaterialsListView(View):

    def get(self, request):

        products_categories = ProductCategory.objects.order_by('id')
        materials_categories = MaterialCategory.objects.order_by('id')
        materials = Material.objects.order_by('price')
        products = Product.objects.order_by('price_lm')

        ctx = {
            'materials' : materials,
            'products' : products,
            'products_categories' : products_categories,
            'materials_categories' : materials_categories,
        }

        return TemplateResponse(request, 'materials/materials_list.html', ctx)

class ProductDetailView(View):

    def get(self, request, product_id):

        product = get_object_or_404(Product, pk=product_id)
        photos = [product.photo_2, product.photo_3, product.photo_4, product.photo_5]

        context = {
            'product' : product,
            'thumbnails' : [thumbnail for thumbnail in photos if thumbnail],
        }

        return TemplateResponse(request, 'materials/product_details.html', context)

class MaterialDetailView(View):

    def get(self, request, material_id):

        material = get_object_or_404(Material, pk=material_id)
        photos = [material.photo_2, material.photo_3 ,material.photo_4, material.photo_5]

        context = {
            'material' : material,
            'thumbnails' : [thumbnail for thumbnail in photos if thumbnail],
        }

        return TemplateResponse(request, 'materials/material_details.html', context)