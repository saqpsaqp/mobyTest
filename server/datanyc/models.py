from django.db import models

# Create your models here.

class Cause(models.Model):
	"""
		Cause of death in New York City (Not normalized)
	"""
	year = models.CharField(max_length=5)
	ethnicity = models.CharField(max_length=50)
	sex = models.CharField(max_length=10)
	cause = models.CharField(max_length=150)
	count = models.CharField(max_length=10)
	percent = models.CharField(max_length=10)
	def __str__(self):
		return '%s' % (self.cause)

