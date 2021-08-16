from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PublicationIndexView(TemplateView):
	template_name = 'publication/publication_index.html'