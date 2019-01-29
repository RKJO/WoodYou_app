from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.mail import send_mass_mail
from django.contrib import messages
from decimal import *

from materials.models import Product, Material
from django.views import View
from .models import Assembly
from .forms import CalculateForm, InquiryModalForm

class CalculationView(View):

    def get(self, request):

        context = {
            'form' : CalculateForm(),
        }

        return TemplateResponse(request, 'calculations/calculation_page.html', context)

    def post(self, request):
        form = CalculateForm(data=request.POST)
        inquiry_form = InquiryModalForm(data=request.POST)

        context = {'form': form}

        if request.POST and form.is_valid():
            surface = form.cleaned_data['surface']
            wood = form.cleaned_data['wood']
            where_to = form.cleaned_data['where_to']

            calculations = self.calculate_cost(surface, wood, where_to)

            context.update({
                'calculations': calculations,
                'values' : form.cleaned_data,
                'inquiry_form' : InquiryModalForm(
                    initial={
                        'surface' : surface,
                        'wood': wood,
                        'where_to': where_to,
                        'message': 'Witam,\nproszę o kontakt w sprawie wyceny tarasu: ' + str(surface) + u'm², ' + str(wood) + ',  ' + str(where_to) +'\n\r'
                    })
                })


            if request.POST and inquiry_form.is_valid():
                name = inquiry_form.cleaned_data['name']
                email = inquiry_form.cleaned_data['email']
                phone = inquiry_form.cleaned_data['phone']
                message = inquiry_form.cleaned_data['message']

                surface = inquiry_form.cleaned_data['surface']
                wood = inquiry_form.cleaned_data['wood']
                where_to = inquiry_form.cleaned_data['where_to']

                calculations = self.calculate_cost(surface, wood, where_to)
                
                message_to_office = (
                    'Zapytanie o taras: '+ str(surface) + u'm², ' + str(wood) + ',  ' + str(where_to), 
                    message + '\n\r' + 'Kontakt do klienta: \n' + name + ' '+ email + ' ' + phone,
                    email,
                    ['biuro@woodyou.waw.pl'])

                message_to_client = (
                    'Potwierdzenie zpytania o taras: '+ str(surface) + u'm², ' + str(wood) + ',  ' + str(where_to),
                    'Dziekujemy za zainteresowanie naszą ofertą, skontaktujemy się z Państwem w najbliższym czasie\n\r Pozdrawiamy, \n Zespół WoodYou\n biuro@woodyou.waw.pl\n +48 531 356 412', 
                    'biuro@woodyou.waw.pl',
                    [email])

                send_mass_mail((message_to_office, message_to_client), fail_silently=False)

                context = {
                    'calculations': calculations,
                    'values' : inquiry_form.cleaned_data,
                    'inquiry_form' : inquiry_form,
                    'form': CalculateForm(
                        initial={
                            'surface' : surface,
                            'wood': wood,
                            'where_to': where_to,
                            })
                }

                messages.success(request, 'Zapytanie o szczegółową oferę zostało poprawnie wysłane. Na Twój adres email zostało również wysłane potwierdzenie')

        return TemplateResponse(request, 'calculations/calculation_page.html', context)

    def calculate_cost(self, surface, wood, where_to):
        # used wood
        wood_price = Product.objects.filter(category_name__product_type=1).filter(used_for_calculate=True).filter(name=wood)[0].price_m2
        wood_cost = wood_price * Decimal(surface)

        # used joist
        joist_price = Product.objects.filter(category_name__product_type=2).filter(used_for_calculate=True).order_by('price_lm')[0].price_lm
        joist_cost = Decimal(joist_price * Decimal('2.5') * Decimal(surface)).quantize(Decimal('.01'), rounding=ROUND_UP)

        # assembly
        assembly_price_to_calculate = Assembly.objects.filter(assembly_type=where_to)[0].price_m2
        if surface <= 16:
            assembly_cost = (assembly_price_to_calculate * Decimal(surface)) + Decimal(800)
            assembly_price = (assembly_cost / Decimal(surface)).quantize(Decimal('1'), rounding=ROUND_UP)
        else:
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
