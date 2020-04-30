from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Client

# Create your views here.

def index(request):	
	latest_client_list = Client.objects.order_by('-creation_date')[:5]
	template = loader.get_template('fichas/index.html')
	context = {'latest_client_list': latest_client_list,}
	return HttpResponse(template.render(context, request))

def client_detail(request, client_id):
	return HttpResponse('Cliente %s: ' % client_id)

