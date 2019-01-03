from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from .models import Product, Material, ProductCategory, MaterialCategory

# Create your views here.

class MaterialsListView(View):

    def get(self, request):

        products_categories = ProductCategory.objects.order_by('id')
        materials_categories = MaterialCategory.objects.order_by('id')
        materials = Material.objects.all()
        products = Product.objects.all()

        ctx = {
            'materials' : materials,
            'products' : products,
            'products_categories' : products_categories,
            'materials_categories' : materials_categories,
        }

        return TemplateResponse(request, 'materials/materials_list.html', ctx)


class MaterialsDetailView(View):

    def get(self, request):
        return TemplateResponse(request, 'materials/material_details.html')