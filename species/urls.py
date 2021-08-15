from django.urls import path
from .views import SpeciesIndexView, SpeciesDetailView

urlpatterns = [
	path('species_index/', SpeciesIndexView.as_view(), name='species_index'),
	path('species_detail/<int:pk>', SpeciesDetailView.as_view(), name='species_detail'),
]