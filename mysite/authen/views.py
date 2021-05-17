import json
import select
from builtins import object
from os.path import abspath

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request
from pkg_resources import require
from django.contrib.auth.models import Group

# Create your views here.
def mylogin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect username or password.')
            return redirect('login')
    else:
        return render(request, template_name='login.html')
    
def signup(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password == password2:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            if role == "no":
                group = Group.objects.get(name='customer')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='store')
                user.groups.add(group)
            user.save() 
            return redirect('login')

        else:
            context['error'] = 'Password Not Match!!!'
            return render(request, template_name='signup.html', context=context)
    return render(request, template_name='signup.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

