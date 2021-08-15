from django.db import models
from django.urls import reverse

# Create your models here.
class Activity(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	date_held = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=100)
	participant = models.CharField(max_length=200)
	description = models.TextField()
	activity_img = models.ImageField('Activity image', null=True, blank=True, upload_to='activity_img/')

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.name + ' | ' + str(self.date_held)

	def get_absolute_url(self):
		return reverse('activity_index')