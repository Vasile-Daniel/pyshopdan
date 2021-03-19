from django.http import HttpResponse
from django.shortcuts import render
#django is a package, 
#shortcuts is a module,
# render is a function 
# HttpResponse is a class 



# /products -> index 
# Uniform Resurce Locator (Address)
def index(request):
	return HttpResponse('Hello world!')


def new(request):
	return HttpResponse('New products')





