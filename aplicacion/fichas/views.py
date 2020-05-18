from django.shortcuts import get_object_or_404,get_list_or_404,render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Client, Ficha
from django.urls import reverse
from django.utils import timezone
from .forms import ClientForm, FichaForm

# Create your views here.

def index(request):	
	latest_client_list = get_list_or_404(Client.objects.order_by('-creation_date'))[:5]
	form = ClientForm(request.POST)
	context = {'latest_client_list': latest_client_list,'form':form}
	if request.method =='POST':
		if form.is_valid():
			client = Client(name = request.POST['name'],
							country = request.POST['country'],
							creation_date = timezone.now())
			client.save()
			return HttpResponseRedirect(reverse('fichas:client_detail', args=(client.id,)))
		return render(request,'fichas/index.html',context)
	return render(request,'fichas/index.html',context)

def client_detail(request, client_id):
	client = get_object_or_404(Client, pk = client_id)
	fichas = client.ficha_set.all()
	print(fichas)
	return render(request,'fichas/client_detail.html',{'client':client,'fichas':fichas})

def ficha_detail(request, ficha_id):
	ficha = get_object_or_404(Ficha, pk = ficha_id)
	return render(request,'fichas/ficha_detail.html',{'ficha':ficha})