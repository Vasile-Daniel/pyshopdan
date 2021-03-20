from django.db import models
# a model este o reprezentare a conceptului lumii reale 
#db este un pachet,  models este un modul 
# Model are toate caracteristicile unui model in aplicatiile Django 
# clasa 'Product' mosteneste clasa 'Model' 
# eu am creat aceasta clasa 
class Product(models.Model):
# definim un atribut (parametru) numit 'name'
# il facem instace cu egal 
# CharField este o clasa 
	name = models.CharField(max_length=255)
	price = models.FloatField()
	stock = models.IntegerField()
	image_url = models.CharField(max_length=2083)

class Offer(models.Model):
	code = models.CharField(max_length=10)
	description = models.CharField(max_length=255)
	discount = models.FloatField()
