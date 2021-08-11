from django.db import models
from django.urls import reverse

# Create your models here.
class Nursery(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	locality = models.CharField(max_length=100)
	area_covered = models.FloatField()
	capacity = models.IntegerField()
	species = models.TextField()
	total_seedling = models.IntegerField()
	description = models.TextField()
	nursery_img = models.ImageField('Nursery Image', null=True, blank=True, upload_to='nursery_img')

	class Meta:
		ordering = ['-date_input']

	def __str__(self):
		return self.name + ' | ' + self.locality

	def get_absolute_url(self):
		return reverse('nursery_index')