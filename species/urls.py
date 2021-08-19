from django.urls import path
from .views import SpeciesIndexView, SpeciesDetailView, indigenous_index, exotic_index

urlpatterns = [
	path('species_index/', SpeciesIndexView.as_view(), name='species_index'),
	path('indigenous_index/', indigenous_index, name='indigenous_index'),
	path('exotic_index/', exotic_index, name='exotic_index'),
	path('species_detail/<int:pk>', SpeciesDetailView.as_view(), name='species_detail'),
]