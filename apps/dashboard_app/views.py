# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..pet_app.models import User
from ..add_app.models import Pet
from django.shortcuts import render,redirect

def dashboard(request):
    if 'email' not in request.session:
        return redirect('/')
    context = {
        "users": User.objects.exclude(id = request.session['id']),
        "pets": User.objects.get(id = request.session['id']).pets.all(),
    }
    return render(request, 'dashboard_app/dashboard.html', context)

def show(request, id):
    context = {
        "user": User.objects.get(id = id),
        "pets": User.objects.get(id = id).pets.all(),
    }
    return render(request, 'dashboard_app/show.html',context)
