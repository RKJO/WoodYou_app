from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalculationView.as_view(), name='kalkulator'),
]