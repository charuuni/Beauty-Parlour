from django.db import models


# Create your models here.
class Branch(models.Model):
     branchname=models.CharField(max_length=10)
     description=models.TextField(max_length=100)
     image=models.ImageField(upload_to='pic',default='null.jpg')

class Service(models.Model):
    servicename = models.CharField(max_length=10)
    branchname = models.CharField(max_length=10)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pic', default='null.jpg')   
    service_name = models.CharField(max_length=100, default='')
    service_type = models.CharField(max_length=100, default='')




    

   

   
    




