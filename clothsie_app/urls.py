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
    # url(r'^$', views.index, name='index'),

    #ITEMS
    # ex: /clothsie_app/item/5/
    # url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /clothsie_app/item/5/post_item/
    # url(r'^(?P<item_id>[0-9]+)/post_item/$', views.post_item, name='post_item'),
    # # ex: /clothsie_app/item/5/delete_item/
    # url(r'^(?P<item_id>[0-9]+)/delete_item/$', views.delete_item, name='delete_item'),
    # # ex: /clothsie_app/item/5/checkout/
    # url(r'^(?P<item_id>[0-9]+)/checkout/$', views.checkout, name='checkout'),
    # # ex: /clothsie_app/item/5/search/
    # url(r'^(?P<item_id>[0-9]+)/search/$', views.search, name='search'),


    #USERS
    # ex: /clothsie_app/users/create_account/
    # url(r'^create_account/$', views.create_account, name='create_account'),
    # # ex: /clothsie_app/users/haykidd/create_account/
    # url(r'^(?P<username>[a-zA-Z]+)/delete_account/$', views.delete_account, name='delete_account'),
    # # ex: /clothsie_app/users/login/
    # url(r'^login/$', views.login, name='login'),
    # # ex: /clothsie_app/users/haykidd/logout/
    # url(r'^(?P<username>[a-zA-Z]+)/logout/$', views.logout, name='logout'),
]


