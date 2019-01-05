from django.shortcuts import render
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
