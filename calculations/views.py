from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from materials.models import Product
from .models import Assembly
from .forms import CalculateForm

class CalculationView(View):

    wood_species = Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).order_by('-name')
    assembly_types = Assembly.objects.order_by('price_m2')

    def get(self, request):

        context = {
            'form': CalculateForm(),
            'wood_species' : self.wood_species,
            'assembly_types' : self.assembly_types,
        }

        return TemplateResponse(request, 'calculations/calculation_page.html', context)

    def post(self, request):

        context = {
            'wood_species' : self.wood_species,
            'assembly_types' : self.assembly_types,
        }

        return TemplateResponse(request, 'calculations/calculation_page.html', context)
