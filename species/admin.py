from django.contrib import admin
from .models import Species

# Register your models here.
class SpeciesAdmin(admin.ModelAdmin):
	list_display = ('local_name', 'species_type',)

admin.site.site_header = 'Greening Sarawak Admin'
admin.site.register(Species, SpeciesAdmin)