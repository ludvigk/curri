from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from . import user_util


def login(request):
    username = request.POST.get('loginusername', '')
    password = request.POST.get('loginpassword', '')
    user = authenticate(username=username, password=password)
    if user is not None or request.user.is_authenticated():
        auth_login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html')


def register(request):
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('confirm-password', '')
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect('/accounts/login/')


def checkusername(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'username' in p.keys():
            name = p['username']
            if user_util.username_present(name):
                return HttpResponse(False)
            else:
                return HttpResponse(True)
