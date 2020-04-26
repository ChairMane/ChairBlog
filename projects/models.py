from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Projects(models.Model):
	title = models.CharField(max_length=100)
	short_description = models.TextField()
	long_description = MarkdownxField()
	project_link = models.URLField(max_length=250)
	def __str__(self):
		return self.title
	
	def formatted_markdown(self):
		return markdownify(self.long_description)
