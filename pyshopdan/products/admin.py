from django.contrib import admin
from .models import Product 


# Register your models here.
# site este un obiect 
# register este un atribut
# Product este un argument 
# o sa ii spuna lui Django ca 
# o sa administreze 'Product' in 'admin'  
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')

admin.site.register(Product, ProductAdmin)

