from django.shortcuts import render
from .models import Nursery
from django.views.generic import ListView, DetailView

# Create your views here.
class NurseryIndexView(ListView):
	model = Nursery
	template_name = 'nursery/nursery_index.html'

class NurseryDetailView(DetailView):
	model = Nursery
	template_name = 'nursery/nursery_detail.html'