from django.db import models

# Create your models here.
class books(models.Model):
    NAME=models.CharField(max_length=300)
    Author=models.CharField(max_length=300)
    Language=models.CharField(max_length=300)
    Release_date=models.CharField(max_length=300)
    image=models.CharField(max_length=10000)
    bdescription=models.CharField(max_length=10000)

