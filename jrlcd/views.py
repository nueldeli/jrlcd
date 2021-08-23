from django.views.generic import TemplateView

class HomeMainView(TemplateView):
	template_name = 'home_main.html'

class HomeEnView(TemplateView):
	template_name = 'home_en.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class PartnershipView(TemplateView):
	template_name = 'partnership.html'

class ForestTypeView(TemplateView):
	template_name = 'forest_type.html'

class WdimView(TemplateView):
	template_name = 'wdim.html'