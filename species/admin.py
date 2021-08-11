from django.contrib import admin
from .models import Species

# Register your models here.
class SpeciesAdmin(admin.ModelAdmin):
	list_display = ('local_name', 'scientific_name',)

admin.site.register(Species, SpeciesAdmin)