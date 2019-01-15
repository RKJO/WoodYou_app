from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

class CalculationView(View):

    def get(self, request):
        return TemplateResponse(request, 'calculations/calculation_page.html')
