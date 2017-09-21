# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse

from .models import User, Item

# Create your views here.


def index(request):
    return HttpResponse('Hello World')


def detail(request, Item):
    return HttpResponse(Item.detail(Item))

# def delete_item(request, item_id):
#	return HttpResponse(Items.delete(item_id))
