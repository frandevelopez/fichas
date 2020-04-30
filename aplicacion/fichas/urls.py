from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	path('<int:client_id>/', views.client_detail, name='client_detail'),
]