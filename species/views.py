from django.shortcuts import render
from .models import Species
from django.views.generic import ListView, DetailView

# Create your views here.

species_object = Species.objects.all()

class SpeciesIndexView(ListView):
	model = Species
	template_name = 'species/species_index.html'

class SpeciesDetailView(DetailView):
	model = Species
	template_name = 'species/species_detail.html'

def indigenous_index(request):
	indigenous_species_index = species_object.filter(species_type__icontains='Indigenous')
	return render(request, 'species/species_indigenous.html', 
		{'indigenous_species_index':indigenous_species_index})

def exotic_index(request):
	exotic_species_index = species_object.filter(species_type__icontains='Exotic')
	return render(request, 'species/species_exotic.html', {
		'exotic_species_index':exotic_species_index
		})