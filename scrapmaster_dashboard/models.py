from django.db import models
from authentication.models import User

# Create your models here.


class ExtraDetails(models.Model):
	"""docstring for ExtraDetails"""
	name = models.CharField(max_length=255)
	details = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.name
		

