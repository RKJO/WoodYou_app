from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

from decimal import *


from materials.models import Product, Material
from .models import Assembly
from .forms import CalculateForm

class CalculationView(View):

    wood_species = Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).order_by('-name')
    assembly_types = Assembly.objects.order_by('price_m2')

    def get(self, request):

        context = {
            'wood_species' : self.wood_species,
            'assembly_types' : self.assembly_types,
        }

        return TemplateResponse(request, 'calculations/calculation_page.html', context)

    def post(self, request):
        if request.method == 'POST':
            surface = request.POST['surface']
            wood = request.POST.get('wood', None)
            where_to = request.POST.get('where_to', None)

        calculations = self.calculate_cost(surface, wood, where_to)

        context = {
            'wood_species' : self.wood_species,
            'assembly_types' : self.assembly_types,
            'values' : request.POST,
            'calculations' : calculations,

        }

        return TemplateResponse(request, 'calculations/calculation_page.html', context)

    def calculate_cost(self, surface, wood, where_to):
        # used wood
        wood_price = self.wood_species.filter(name=wood)[0].price_m2
        wood_cost = wood_price * Decimal(surface)
        # used joist
        joist_price = Product.objects.filter(category_name__product_type=2).filter(used_for_calculate=True).order_by('price_lm')[0].price_lm
        joist_cost = Decimal(joist_price * Decimal('2.5') * Decimal(surface)).quantize(Decimal('.01'), rounding=ROUND_UP)
        
        # assembly
        assembly_price = self.assembly_types.filter(assembly_type=where_to)[0].price_m2
        assembly_cost = assembly_price * Decimal(surface)

        # screws
        screws_pice = Material.objects.filter(category_name__material_type=2).filter(used_for_calculate=True).order_by('price')[0].price
        screws_cost = screws_pice * Decimal((int(surface)/6)).quantize(Decimal('1'), rounding=ROUND_UP)

        # oil
        oil_price = Material.objects.filter(category_name__material_type=1).filter(used_for_calculate=True).order_by('price')[0].price
        oil_cost = oil_price * Decimal((int(surface)/25)).quantize(Decimal('1'), rounding=ROUND_UP)

        # total
        total_cost = sum([wood_cost, joist_cost, screws_cost, oil_cost, assembly_cost])



        return {
            'wood_price' : wood_price,
            'wood_cost' : wood_cost,
            'joist_price' : joist_price,
            'joist_cost' : joist_cost,
            'screws_pice' : screws_pice,
            'screws_cost' : screws_cost,
            'oil_price' : oil_price,
            'oil_cost' : oil_cost,
            'assembly_price' : assembly_price,
            'assembly_cost' : assembly_cost,
            'total_cost' : total_cost
        }