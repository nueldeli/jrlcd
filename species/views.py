from django.shortcuts import render
from .models import Species
from django.views.generic import ListView

# Create your views here.
class SpeciesIndexView(ListView):
	model = Species
	template_name = 'species/species_index.html'