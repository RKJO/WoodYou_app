from django.urls import path

from . import views

urlpatterns = [
    path('', views.MaterialsListView.as_view(), name="materialy"),
    path('product/<str:product_name>', views.ProductDetailView.as_view(), name='produkt'),
    path('<str:material_name>', views.MaterialDetailView.as_view(), name='material'),

]