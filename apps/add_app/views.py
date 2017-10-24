"""
Add App
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Pet
from ..pet_app.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def pet_new(request):
    if 'email' not in request.session:
        return redirect('/')
    return render(request, 'add_app/addpet.html')
def pet_create(request):
    errors = Pet.objects.pet_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
    else:
        messages.success(request, "Congrats on the new pet!")
        new_pet = Pet.objects.create_pet(request)
        User.objects.get(id=request.session['id']).pets.add(new_pet)
    return redirect('/pet/new')

def pet_delete(request, id):
    Pet.objects.get(id = id).delete()
    return redirect('/dashboard')
