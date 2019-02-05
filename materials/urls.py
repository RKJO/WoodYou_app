from django.urls import path

from . import views

urlpatterns = [
    path('', views.MaterialsListView.as_view(), name="materialy"),
    path('produkt/<int:product_id>', views.ProductDetailView.as_view(), name='produkt'),
    path('<int:material_id>', views.MaterialDetailView.as_view(), name='material'),

]