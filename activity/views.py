from django.shortcuts import render
from .models import Activity
from django.views.generic import ListView, DetailView

# Create your views here.
class ActivityIndexView(ListView):
	model = Activity
	template_name = 'activity/activity_index.html'

class ActivityDetailView(DetailView):
	model = Activity
	template_name = 'activity/activity_detail.html'
	