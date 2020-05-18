from django import forms 
from django_countries.fields import CountryField
from .models import Client, Leather, Hardware, Lining

class ClientForm(forms.Form):
	name = forms.CharField(label='Client name', max_length=100)
	country = CountryField().formfield()

class SupplierForm(forms.Form):

	name = forms.CharField(label="Supplier name", max_length=200)
	country = forms.CharField(label="Supplier country", max_length=200)
 
class FichaForm(forms.Form):

	name = forms.CharField(max_length=200)
	client = forms. ModelChoiceField (label='Client', queryset = Client.objects.all())
	price = forms.DecimalField(label='Price')
	upper = forms.ModelChoiceField(label='Leather', queryset = Leather.objects.all())
	lining = forms.ModelChoiceField(label='Lining', queryset = Lining.objects.all())
	edge_paint = forms.CharField(label='edge_paint', max_length=200)
	thread = forms.CharField(label='Price', max_length=200)
	sku = forms.CharField(label='Price', max_length=200)

# class Color(forms.Form):

# 	name = forms.CharField(max_length=200)

# class Leather(forms.Form):

# 	name = forms.CharField(max_length=200)
# 	supplier = forms.ModelChoiceField('Supplier',on_delete = models.CASCADE,default=None)
# 	price = forms.DecimalField(max_digits=5,default=0, decimal_places=2)
# 	moq = forms.DecimalField(max_digits=5,default=0, decimal_places=2)

# class Hardware(forms.Form):

# 	name = forms.CharField(max_length=200)
# 	supplier = forms.ModelChoiceField('Supplier',on_delete = models.CASCADE, default=None)
# 	price = forms.DecimalField(max_digits=5,default=0, decimal_places=2)
# 	moq = forms.DecimalField(max_digits=5,default=0, decimal_places=2)

# class Lining(forms.Form):

# 	name = forms.CharField(max_length=200)
# 	supplier = forms.ModelChoiceField('Supplier',on_delete = models.CASCADE,default=None)
# 	price = forms.DecimalField(max_digits=5,default=0, decimal_places=2)
# 	roll_height = forms.DecimalField(max_digits=5,default=0, decimal_places=2)
# 	moq = forms.DecimalField(max_digits=5,default=0, decimal_places=2)
