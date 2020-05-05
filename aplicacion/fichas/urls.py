from django.urls import path
from . import views

app_name = 'fichas'
urlpatterns = [
	path('',views.index),
	path('<int:client_id>/', views.client_detail, name='client_detail'),
]