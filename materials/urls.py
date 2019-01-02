from django.urls import path

from . import views

urlpatterns = [
    path('', views.MaterialsListView.as_view(), name="materialy"),
]