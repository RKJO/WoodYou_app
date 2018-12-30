from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View


# Create your views here.

class MaterialsListView(View):

    def get(self, request):
        return TemplateResponse(request, 'materials/materials_list.html')


class MaterialsDetailView(View):

    def get(self, request):
        return TemplateResponse(request, 'materials/material_details.html')