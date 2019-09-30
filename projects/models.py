from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=200)
	slug_name = models.SlugField(max_length=255, unique=True)
	languages = models.CharField(max_length=255)
	pic = models.CharField(max_length=25)
	github = models.CharField(max_length=255)
	demo = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	description = models.TextField()

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e, %Y')
	def __str__(self):
		return self.title