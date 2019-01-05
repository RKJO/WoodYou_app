from django.urls import path

from . import views

urlpatterns = [
    path('', views.RealizationsListView.as_view(), name="realizacje"),
]