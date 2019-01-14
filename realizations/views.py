from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.views import View
from .models import Ralization
from django.core.paginator import Paginator

class RealizationsListView(View):

    def get(self, request):

        realizations = Ralization.objects.order_by('-realization_date')

        paginator = Paginator(realizations, 6)
        page = request.GET.get('page')
        paged_realizations = paginator.get_page(page)

        context = {
            'realizations' : paged_realizations,
        }        

        return TemplateResponse(request, 'realizations/realizations_list.html', context)

class RealizationDetailView(View):

    def get(self, request, realization_id):

        realization = get_object_or_404(Ralization, pk=realization_id)
        products = [realization.used_products1, realization.used_products2, realization.used_materials1, realization.used_materials2, realization.used_materials3]

        context = {
            'realization' : realization,
            'thumbnails' : [realization.photo_2, realization.photo_3 ,realization.photo_4, realization.photo_5],
            'products' : [product for product in products if product] ,
        }

        return TemplateResponse(request, 'realizations/realization_detail.html', context)
