from django.contrib import admin
from .models import Nursery

# Register your models here.
class NurseryAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Nursery, NurseryAdmin)