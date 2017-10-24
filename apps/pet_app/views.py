from __future__ import unicode_literals
from models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render(request, "pet_app/index.html")

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['errors']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, "Successfully registered!")
        User.objects.createUser(request.POST)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['errors']:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['f_name'] = results['user'].f_name
        request.session['id'] = results['user'].id
        request.session['email'] = results['user'].email
        return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect ('/')
