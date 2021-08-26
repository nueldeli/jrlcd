from django.shortcuts import render
from .models import Forest
from django.views.generic import ListView, DetailView

# Create your views here.
class ForestIndexView(ListView):
	model = Forest
	template_name = 'forest/forest_index.html'

class ForestDetailView(DetailView):
	model = Forest
	template_name = 'forest/forest_detail.html'