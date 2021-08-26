from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Forest(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	description = RichTextUploadingField(blank=True)
	forest_img = models.ImageField('Forest Image', null=True, blank=True, upload_to='forest_img/')

	class Meta:
		ordering = ['date_input']


	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('forest_index')