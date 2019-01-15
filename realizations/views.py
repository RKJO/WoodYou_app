from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.views import View
from .models import Ralization
from materials.models import Product
from django.core.paginator import Paginator

class RealizationsListView(View):

    def get(self, request):

        # realizations
        queryset_list = Ralization.objects.order_by('-realization_date')
        used_woods = Ralization.objects.order_by('-realization_date')


        # powierzchnia_od
        if 'powierzchnia_od' in request.GET:
            area_from = request.GET['powierzchnia_od']
            if area_from:
                queryset_list= queryset_list.filter(area__gte=area_from)

        # powierzchnia_do
        if 'powierzchnia_do' in request.GET:
            area_to = request.GET['powierzchnia_do']
            if area_to:
                queryset_list= queryset_list.filter(area__lte=area_to)

        # rodzaj_drewna
        if 'rodzaj_drewna' in request.GET:
            wood_type = request.GET['rodzaj_drewna']
            if wood_type:
                queryset_list= queryset_list.filter(used_wood__name__iexact=wood_type)

        paginator = Paginator(queryset_list, 6)
        page = request.GET.get('page')
        paged_realizations = paginator.get_page(page)

        context = {
            'used_woods': {product.used_wood for product in used_woods},
            'realizations' : paged_realizations,
            'values' : request.GET,
        }        

        return TemplateResponse(request, 'realizations/realizations_list.html', context)

class RealizationDetailView(View):

    def get(self, request, realization_id):

        realization = get_object_or_404(Ralization, pk=realization_id)
        photos = [realization.photo_2, realization.photo_3 ,realization.photo_4, realization.photo_5]
        products = [realization.used_products1, realization.used_products2, realization.used_materials1, realization.used_materials2, realization.used_materials3]

        context = {
            'realization' : realization,
            'thumbnails' : [thumbnail for thumbnail in photos if thumbnail],
            'products' : [product for product in products if product],
        }

        return TemplateResponse(request, 'realizations/realization_detail.html', context)
