from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Properties(models.Model):
    property = models.AutoField(primary_key = True)
    location = models.CharField(max_length = 100)
    details = models.TextField()
    Process = models.CharField(max_length=100, default='available')

class Images(models.Model):
    properties = models.ForeignKey(Properties, on_delete =models.CASCADE)
    # image_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length= 100)
    date_posted = models.DateTimeField(max_length= 100, null = True, blank = True)

class Owners(models.Model):
    # Owner_id
    firstname = models.CharField(max_length= 100)
    lastname = models.CharField(max_length = 100)
    emailAdress = models.CharField(max_length = 100, unique =True)
    telphone = models.CharField(max_length = 100)


class Bill(models.Model):
    properties = models.ForeignKey(Properties, on_delete =models.CASCADE)
    date_paid = models.DateTimeField( null = True, blank = True)
    # Process = models.CharField(max_length=100, default='available')
    amount_paid = models.IntegerField()
    amount_in_words = models.CharField(max_length = 150)

class Expenses(models.Model):
    properties = models.ForeignKey(Properties, on_delete =models.CASCADE)
    amount = models.IntegerField()
    reason = models.TextField()
    Date = models.DateTimeField(null = True, blank = True)

class Documents(models.Model):
    properties = models.ForeignKey(Properties, on_delete =models.CASCADE)
    files = models.FileField()
    percantage = models.IntegerField()









    

