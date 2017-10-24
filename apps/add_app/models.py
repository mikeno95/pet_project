# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..pet_app.models import User
from django.db import models

def check_string(string):
        for char in string:
            if char.isdigit():
                return True
        return False

class PetManager(models.Manager):
    def pet_validator(self, postData):
        errors = []
        if not len(postData['name']):
            errors.append('Please enter a name')
        if not len(postData['species']):
            errors.append("Please enter your pet's species")
        if check_string(postData['species']):
            errors.append("Your pet's species cannot contain a digit")
        return errors

    def create_pet(self, request):
        return self.create(name = request.POST['name'], species = request.POST['species'])





class Pet(models.Model):
    name = models.CharField(max_length=250)
    species = models.CharField(max_length=100)
    owner = models.ManyToManyField(User, related_name='pets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PetManager()
