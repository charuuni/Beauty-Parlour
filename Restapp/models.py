from django.db import models

# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    number=models.IntegerField()

class Demo(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    
