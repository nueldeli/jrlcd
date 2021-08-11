from django.db import models
from django.urls import reverse

# Create your models here.
class Species(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	local_name = models.CharField(max_length=100)
	scientific_name = models.CharField(max_length=100)
	origin = models.CharField(max_length=100)
	description = models.TextField()
	species_img = models.ImageField('Species Image', null=True, blank=True, upload_to='species_img')

	class Meta:
		ordering = ['-date_input']

	def __str__(self):
		return self.local_name + ' | ' + self.scientific_name

	def get_absolute_url(self):
		return reverse('species_index')
