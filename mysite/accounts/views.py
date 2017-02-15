from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from . import user_util
from django.core import validators
from django.http import HttpResponseRedirect


def login(request):
    username = request.POST.get('loginusername', '')
    password = request.POST.get('loginpassword', '')
    user = authenticate(username=username, password=password)
    if user is not None or request.user.is_authenticated():
        auth_login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html')


def register(request):
    p = request.POST
    username = p.get('username', '')
    email = p.get('email', '')
    password = p.get('password', '')
    confirm_password = p.get('confirm-password', '')
    if user_util.username_valid(username) or user_util.email_present(email):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect('/accounts/login/')


def checkusername(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'username' in p.keys():
            name = p['username']
            return  HttpResponse(user_util.username_valid(name))
    return HttpResponse('Invalid request')


def checkemail(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'email' in p.keys():
            email = p['email']
            return HttpResponse(user_util.email_valid(email))
    return HttpResponse('Invalid request')
