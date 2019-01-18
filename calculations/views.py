from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from decimal import *

from materials.models import Product, Material
from .models import Assembly
from .forms import CalculateForm

class CalculationView(View):

    def get(self, request):

        context = {
            'form' : CalculateForm(),
        }

        return TemplateResponse(request, 'calculations/calculation_page.html', context)

    def post(self, request):
        form = CalculateForm(data=request.POST)
        context = {'form': form}

        if form.is_valid():
            surface = form.cleaned_data['surface']
            wood = form.cleaned_data['wood']
            where_to = form.cleaned_data['where_to']

            calculations = self.calculate_cost(surface, wood, where_to)

            context.update({
                'calculations': calculations,
                'values' : form.cleaned_data,
            })

        return TemplateResponse(request, 'calculations/calculation_page.html', context)

    def calculate_cost(self, surface, wood, where_to):
        # used wood
        wood_price = Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).filter(name=wood)[0].price_m2
        wood_cost = wood_price * Decimal(surface)

        # used joist
        joist_price = Product.objects.filter(category_name__product_type=2).filter(used_for_calculate=True).order_by('price_lm')[0].price_lm
        joist_cost = Decimal(joist_price * Decimal('2.5') * Decimal(surface)).quantize(Decimal('.01'), rounding=ROUND_UP)

        # assembly
        assembly_price = Assembly.objects.filter(assembly_type=where_to)[0].price_m2
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
