from django.urls import path 
from . import views  
# django is a package 
# urls is a module 
# path is a function 


#/products 
#/products/1/detail
#/products/new 

urlpatterns = [
	path('', views.index),
	path('new', views.new)
]