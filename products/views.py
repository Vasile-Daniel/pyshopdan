from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
#django is a package, 
#shortcuts is a module,
# render is a function 
# HttpResponse is a class 



# /products -> index 
# Uniform Resurce Locator (Address)
def index(request):
	products = Product.objects.all()
	return render(request, 'index.html', {'products': products})
	#return HttpResponse('Hello world!')


def new(request):
	return HttpResponse('New products')





