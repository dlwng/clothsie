# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
	items_bought = models.ForeignKey(Items, on_delete=models.CASCADE)
	items_selling = models.ForeignKey(Items, on_delete=models.CASCADE) 
	items_sold = models.ForeignKey(Items, on_delete=models.CASCADE)

class Items(models.Model):
	comments = models.TextField()
	date_added = models.DateField()
	date_purchased = models.DateField()
	zipcode = models.IntegerField()
	price = models.FloatField()
	size = models.CharField(max_length=10)
	category = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	brand = models.CharField(max_length=50)
	description = models.TextField()