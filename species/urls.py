from django.urls import path
from .views import SpeciesIndexView

urlpatterns = [
	path('species_index/', SpeciesIndexView.as_view(), name='species_index'),
]