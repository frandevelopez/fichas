from django.db import models

# Create your models here.

class Ficha(models.Model):
	style_name = models.CharField(max_length=200)
	client = models.ForeignKey('Client',on_delete=models.CASCADE)
	style_price=models.IntegerField(default=0)

class Client(models.Model):
	client_name = models.CharField(max_length=200)
	client_country = models.CharField(max_length=200)