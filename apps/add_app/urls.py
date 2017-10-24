"""
Add App
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pet/new$', views.pet_new),
    url(r'^pet/create$', views.pet_create),
    url(r'^pet/delete/(?P<id>\d+)$', views.pet_delete),
]
