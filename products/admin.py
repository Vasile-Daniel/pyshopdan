from django.contrib import admin
from .models import Product, Offer 


# Register your models here.
# site este un obiect 
# register este un atribut
# Product este un argument 
# o sa ii spuna lui Django ca 
# o sa administreze 'Product' in 'admin'  
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
	list_display = ('code', 'discount')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)

