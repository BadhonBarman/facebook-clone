from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=100, default='')
	password = models.CharField(max_length=200)

	def register(self):
		self.save()