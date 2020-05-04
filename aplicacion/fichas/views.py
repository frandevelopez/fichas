from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Client, Ficha

# Create your views here.

def index(request):	
	latest_client_list = Client.objects.order_by('-creation_date')[:5]
	context = {'latest_client_list': latest_client_list,}
	return render(request,'fichas/index.html',context)

def client_detail(request, client_id):
	client = Client.objects.get(pk=client_id)
	fichas = Ficha.objects.filter(client=client_id)
	return render(request,'fichas/client_detail.html',{'client':client, 'fichas':fichas})

