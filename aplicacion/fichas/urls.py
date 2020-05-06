from django.urls import path
from . import views

app_name = 'fichas'
urlpatterns = [
	path('',views.index, name='index'),
	path('client/<int:client_id>/', views.client_detail, name='client_detail'),
	path('ficha/<int:ficha_id>/', views.ficha_detail, name='ficha_detail'),
	path('client_post/', views.client_post, name='client_post')
]