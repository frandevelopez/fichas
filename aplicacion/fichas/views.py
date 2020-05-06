from django.shortcuts import get_object_or_404,get_list_or_404,render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Client, Ficha
from django.urls import reverse
from django.utils import timezone

# Create your views here.

def index(request):	
	latest_client_list = get_list_or_404(Client.objects.order_by('-creation_date'))[:5]
	context = {'latest_client_list': latest_client_list,}
	return render(request,'fichas/index.html',context)

def client_detail(request, client_id):
	client = get_object_or_404(Client, pk=client_id)
	return render(request,'fichas/client_detail.html',{'client':client})

def ficha_detail(request, ficha_id):
	ficha = get_object_or_404(Ficha, pk=ficha_id)
	return render(request,'fichas/ficha_detail.html',{'ficha':ficha})

def client_post(request):
	try:
		client = Client(name= request.POST['name'],
					    country= request.POST['country'],
					    creation_date= timezone.now())
		client.save()
	except:
		raise Http404('ni idea chacho')	
	return HttpResponseRedirect(reverse('fichas:index'))