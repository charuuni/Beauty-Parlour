from django.db import models
from Adminapp . models import *
from django.db.models import Sum


# Create your models here.
class Contact(models.Model):
    name1=models.CharField(max_length=10)
    email1=models.EmailField(default=0)
    number=models.IntegerField(default=0)
    message1=models.CharField(max_length=1000)

class Register(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=20)

class Cart(models.Model):
    serviceid = models.ForeignKey(Service, on_delete=models.CASCADE)
    userid = models.ForeignKey(Register, on_delete=models.CASCADE)
    total = models.IntegerField(default=0) 
    status = models.IntegerField(default=0)
 

class Booking(models.Model):
    cartid = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    userid = models.ForeignKey(Register, on_delete=models.CASCADE,default=12)
    status = models.IntegerField()
    date = models.DateField(default=0)
    time = models.TimeField(default=0)

   
   
   

