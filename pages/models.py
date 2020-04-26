from django.db import models

class Page(models.Model):
	title = models.CharField(max_length=100)
	short_description = models.TextField()
	page_url = models.CharField(max_length=40, default='')

	def __str__(self):
		return self.title