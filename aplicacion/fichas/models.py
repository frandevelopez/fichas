from django.db import models
from django.utils import timezone

# Create your models here.

class Ficha(models.Model):
	style_name = models.CharField(max_length=200)
	client = models.ForeignKey('Client',on_delete=models.CASCADE)
	style_price=models.DecimalField(max_digits=5,default=0, decimal_places=2)

	def __str__(self):
		return self.style_name


class Client(models.Model):
	client_name = models.CharField(max_length=200)
	client_country = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date published', default=timezone.now())

	def __str__(self):
		return self.client_name