"""clothsie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # ex: /clothsie_app/
    url(r'^$', views.index, name='index'),

    # ITEMS
    # ex: /clothsie_app/api/v1/create_item/
    url(r'^api/v1/create_item/', views.create_item, name='create-item'),
    # ex: /clothsie_app/api/v1/read_item/5/
    url(r'^api/v1/read_item/(?P<item_id>[0-9]+)/$', views.read_item, name='read-item'),
    # ex: /clothsie_app/api/v1/update_item/5/
    url(r'^api/v1/update_item/(?P<item_id>[0-9]+)/$', views.update_item, name='update-item'),
    #  ex: /clothsie_app/item/5/delete_item/1/
    url(r'^api/v1/delete_item/(?P<item_id>\d+)/$', views.delete_item, name='delete-item'),

    # USERS
    # ex: /clothsie_app/api/v1/create_user/
    url(r'^api/v1/create_user/', views.create_user, name='create-user'),
    # ex: /clothsie_app/api/v1/read_user/1/
    url(r'^api/v1/user/(?P<username>[0-9]+)/$', views.read_user, name='read-user'),
    # ex: /clothsie_app/api/v1/update_user/1/
    url(r'^api/v1/update_user/(?P<username>[0-9]+)/$', views.update_user, name='update-user'),
    # ex: /clothsie_app/api/v1/delete_user/2/
    url(r'^api/v1/delete_user/(?P<username>\d+)/$', views.delete_user, name='delete-user'),
]
