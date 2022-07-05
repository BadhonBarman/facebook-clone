from django.db import models

# Create your models here.
class UserData(models.Model):
	name = models.CharField(max_length=100, default='')
	password = models.CharField(max_length=200)

	# before/after login
	cover_img= models.ImageField(upload_to="images", default='')
	user_bio=models.CharField(max_length=100, default='', blank=True)

	def register(self):
		self.save()

