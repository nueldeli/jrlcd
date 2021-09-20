from django.db import models
from django.urls import reverse

# Create your models here.
TYPE_CHOICES = (
		("INDIGENOUS", "Indigenous"),
		("EXOTIC", "Exotic"),
	)

class Species(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	local_name = models.CharField(max_length=100)
	species_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='INDIGENOUS')
	species_img = models.ImageField('Species Image', null=True, blank=True, upload_to='species_img')
	species_thumbnail = models.ImageField('Species thumbnail', null=True, blank=True, upload_to='species_thumbnail')

	class Meta:
		ordering = ['-date_input']

	def __str__(self):
		return self.local_name

	def get_absolute_url(self):
		return reverse('species_index')
