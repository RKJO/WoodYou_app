from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from materials.models import Product
from .models import Assembly

class CalculationView(View):

    def get(self, request):

        wood_species = Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).order_by('-name')
        assembly_type = Assembly.objects.order_by('price_m2')

        context = {
            'wood_species' : wood_species,
            'assembly_type' : assembly_type,
        }

        return TemplateResponse(request, 'calculations/calculation_page.html', context)
