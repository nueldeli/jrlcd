from django.views.generic import TemplateView

class HomeMainView(TemplateView):
	template_name = 'home_main.html'

class HomeEnView(TemplateView):
	template_name = 'home_en.html'