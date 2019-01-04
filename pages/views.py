from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

from realizations.models import Ralization


class IndexView(View):

    def get(self, request):

        realizations = Ralization.objects.order_by('-realization_date')[:3]

        ctx = {
            'realizations' : realizations
        }

        return TemplateResponse(request, 'pages/index.html', ctx)