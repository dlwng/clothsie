# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
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
	item_id = models.IntegerField()

	# def detail(item_id):
	# 	return (comments + date_added + date_purchased + zipcode + price + size 
	# 		+ category + color + brand + description)

#def delete(item_id):

#	return("Item Deleted")

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	items_bought = models.ForeignKey(Item, related_name='items_bought', on_delete=models.CASCADE)
	items_selling = models.ForeignKey(Item, related_name='items_selling', on_delete=models.CASCADE)
	items_sold = models.ForeignKey(Item, related_name='items_sold', on_delete=models.CASCADE)
#def delete_item(item_id, username):