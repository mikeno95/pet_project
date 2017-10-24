# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def check_string(string):
    for char in string:
        if not char.isalpha():
            return True
    return False

class UserManager(models.Manager):
    def loginVal(self,postData):
        results = {'errors':[], 'user': None}
        email_matches = self.filter(email = postData['email'])
        if len(email_matches) == 0:
            results['errors'].append('Please check to see if your email or password are correct.')
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check to see if your email or password are correct.')
        return results

    def registerVal(self,postData):
        results = {'errors':[], 'user': None}
        if len(postData['f_name']) < 2:
            results['errors'].append('First Name is too short')
        if check_string(postData['f_name']):
            results['errors'].append("Please enter a valid first name.")
        if len(postData['l_name']) < 2:
            results['errors'].append('Last Name is too short')
        if check_string(postData['l_name']):
            results['errors'].append("Please enter a valid last name.")
        sameFirstName = self.filter(f_name = postData['f_name'])
        if len(sameFirstName):
            for i in sameFirstName:
                if postData['l_name'] == i.l_name:
                    results['errors'].append("Cannot have the same first and last name as another user")
        try:
            validate_email(postData['email'])
        except ValidationError:
            results['errors'].append("Please enter a valid email!")
        if len(postData['password']) < 8:
            results['errors'].append('Password is too short')
        if postData['password'] != postData['c_password']:
            results['errors'].append('Password does not match')
        user = self.filter(email= postData['email'])
        if len(user):
            results['errors'].append('email already exists')
        return results

    def createUser(self, postData):
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(f_name=postData['f_name'], l_name=postData['l_name'], email=postData['email'], password= password)

class User(models.Model):
    email = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
