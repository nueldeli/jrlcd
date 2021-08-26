from django.contrib import admin
from .models import Forest

# Register your models here.
class ForestAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Forest, ForestAdmin)