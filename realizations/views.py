from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

# Create your views here.

class RealizationsListView(View):

    def get(self, request):

        return TemplateResponse(request, 'realizations/realizations_list.html')