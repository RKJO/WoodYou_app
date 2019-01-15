from django.urls import path

from . import views

urlpatterns = [
    path('', views.RealizationsListView.as_view(), name="realizacje"),
    path('<int:realization_id>', views.RealizationDetailView.as_view(), name='realizacja'),

]