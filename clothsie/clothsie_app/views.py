# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import User, Item

# Create your views here.

# Test hello


def index(request):
    return HttpResponse('Hello! Welcome to Clothsie!')

# Error message


def get_error(request):
    error_dict = {}
    error_dict[1] = "This is an error lol"
    return JsonResponse(error_dict, safe=False)

# ITEM APIS


@csrf_exempt
def create_item(request):
    if request.method == 'GET':
        return get_error(request)
    elif request.method == 'POST':
        comments = request.POST.get('comments', "no comment")
        date_added = request.POST.get('date_added', "9999-01-01")
        date_purchased = request.POST.get('date_purchased', "9999-01-01")
        zipcode = request.POST.get('zipcode', "00000")
        price = request.POST.get('price', "5")
        category = request.POST.get('category', "no category")
        color = request.POST.get('color', "no color")
        brand = request.POST.get('brand', "no brand")
        description = request.POST.get('description', "no description")
        item_id = request.POST.get('item_id', "-1")
        Item.objects.create(comments=comments,
                            date_added=date_added,
                            date_purchased=date_purchased,
                            zipcode=zipcode,
                            price=price,
                            category=category,
                            color=color,
                            brand=brand,
                            item_id=item_id)

        new_dict = {}
        new_dict[1] = "Successfully Added!"
        return JsonResponse(new_dict[1], safe=False)


def read_item(request, item_id):
    if request.method == 'GET':
        obj = Item.objects.get(pk=item_id)
        data = model_to_dict(obj)
        return JsonResponse(data, safe=False)
    else:
        return get_error(request)


@csrf_exempt
def update_item(request, item_id):
    if request.method == 'GET':
        return get_error(request)
    elif request.method == 'POST':
        for key in request.POST:
            if key == "comments":
                comments = request.POST.get('comments', "no comment")
                Item.objects.filter(pk=item_id).update(comments=comments)
            if key == "date_purchased":
                date_purchased = request.POST.get('date_purchased', "9999-01-01")
                Item.objects.filter(pk=item_id).update(date_purchased=date_purchased)
            if key == "zipcode":
                zipcode = request.POST.get('zipcode', "00000")
                Item.objects.filter(pk=item_id).update(zipcode=zipcode)
            if key == "price":
                price = request.POST.get('price', "5")
                Item.objects.filter(pk=item_id).update(price=price)
            if key == "category":
                category = request.POST.get('category', "no category")
                Item.objects.filter(pk=item_id).update(category=category)
            if key == "color":
                color = request.POST.get('color', "no color")
                Item.objects.filter(pk=item_id).update(color=color)
            if key == "brand":
                brand = request.POST.get('brand', "no brand")
                Item.objects.filter(pk=item_id).update(brand=brand)
            if key == "description":
                description = request.POST.get('description', "no description")
                Item.objects.filter(pk=item_id).update(description=description)
        new_dict = {}
        new_dict[1] = "Successfully Updated!"
        return JsonResponse(new_dict[1], safe=False)


@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        obj = Item.objects.get(pk=item_id)
        obj.delete()
        valid_dict = {}
        valid_dict[1] = "Successfully Deleted!"
        return JsonResponse(valid_dict[1], safe=False)
    else:
        return get_error(request)


# USER APIS]

@csrf_exempt
def create_user(request):
    if request.method == 'GET':
        return get_error(request)
    elif request.method == 'POST':
        first_name = request.POST.get('first_name', "no first")
        last_name = request.POST.get('last_name', "no last")
        username = request.POST.get('username', "no name")
        password = request.POST.get('password', "no pass")
        email = request.POST.get('email', "no email")
        items_bought = request.POST.get('items_bought')
        items_selling = request.POST.get('items_selling')
        items_sold = request.POST.get('items_sold')
        User.objects.create(first_name=first_name,
                            last_name=last_name,
                            username=username,
                            password=password,
                            email=email,
                            items_bought=items_bought,
                            items_selling=items_selling,
                            items_sold=items_sold)
        new_dict = {}
        new_dict[1] = "Successfully Added!"
        return JsonResponse(new_dict[1], safe=False)


def read_user(request, username):
    if request.method == 'GET':
        obj = User.objects.get(pk=username)
        data = model_to_dict(obj)
        return JsonResponse(data, safe=False)
    else:
        return get_error(request)


@csrf_exempt
def update_user(request, username):
    if request.method == 'GET':
        return get_error(request)
    elif request.method == 'POST':
        for key in request.POST:
            if key == "first_name":
                first_name = request.POST.get('first_name', "no first name")
                Item.objects.filter(pk=username).update(first_name=first_name)
            if key == "last_name":
                last_name = request.POST.get('last_name', "no last name")
                Item.objects.filter(pk=username).update(last_name=last_name)
            if key == "username":
                username = request.POST.get('username', "00000")
                Item.objects.filter(pk=username).update(username=username)
            if key == "password":
                password = request.POST.get('password', "5")
                Item.objects.filter(pk=username).update(password=password)
            if key == "email":
                email = request.POST.get('email', "no email")
                Item.objects.filter(pk=username).update(email=email)
            if key == "items_bought":
                items_bought = request.POST.get('items_bought')
                Item.objects.filter(pk=username).update(items_bought=items_bought)
            if key == "items_selling":
                items_selling = request.POST.get('items_selling')
                Item.objects.filter(pk=username).update(items_selling=items_selling)
            if key == "items_sold":
                items_sold = request.POST.get('items_sold')
                Item.objects.filter(pk=username).update(items_sold=items_sold)
        new_dict = {}
        new_dict[1] = "Successfully Updated!"
        return JsonResponse(new_dict[1], safe=False)


@csrf_exempt
def delete_user(request, username):
    if request.method == 'DELETE':
        obj = Item.objects.get(pk=username)
        obj.delete()
        valid_dict = {}
        valid_dict[1] = "Successfully Deleted!"
        return JsonResponse(valid_dict[1], safe=False)
    else:
        return get_error(request)
