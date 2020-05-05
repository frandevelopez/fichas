from django.db import models
from django.utils import timezone

# Create your models here.

class Supplier(models.Model):
	name = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Client(models.Model):
	name = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date published', default=timezone.now())

	def __str__(self):
		return self.name

class Ficha(models.Model):
	name = models.CharField(max_length=200)
	client = models.ForeignKey('Client',on_delete=models.CASCADE,default=None)
	price = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	upper = models.ForeignKey('Leather',on_delete=models.CASCADE,default=None)
	lining = models.ForeignKey('Lining',on_delete=models.CASCADE,default=None)
	edge_apint = models.CharField(max_length=200,default=None)
	thread = models.CharField(max_length=200,default=None)
	sku = models.CharField(max_length=200)

	creation_date = models.DateTimeField('date published', default=timezone.now())

	def __str__(self):
		return self.name

class Color(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Leather(models.Model):
	name = models.CharField(max_length=200)
	supplier = models.ForeignKey('Supplier',on_delete = models.CASCADE,default=None)
	price = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	moq = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	def __str__(self):
		return self.name

class Hardware(models.Model):
	name = models.CharField(max_length=200)
	supplier = models.ForeignKey('Supplier',on_delete = models.CASCADE, default=None)
	price = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	moq = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	def __str__(self):
		return self.name

class Lining(models.Model):
	name = models.CharField(max_length=200)
	supplier = models.ForeignKey('Supplier',on_delete = models.CASCADE,default=None)
	price = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	roll_height = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	moq = models.DecimalField(max_digits=5,default=0, decimal_places=2)
	def __str__(self):
		return self.name


