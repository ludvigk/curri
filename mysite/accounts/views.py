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
import random
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator


def login(request):
    username = request.POST.get('loginusername', '')
    password = request.POST.get('loginpassword', '')
    user = authenticate(username=username, password=password)
    if user is not None or request.user.is_authenticated():
        auth_login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html')


def register(request):
    try:
        p = request.GET.copy()
        username = p.get('username', '')
        email = p.get('email', '')
        password = p.get('password', '')
        assert(user_util.email_valid(email))
        assert(user_util.username_valid(username))
        user = User.objects.create_user(username, email, password)
        user.save()
        user.is_active = False
        try:
            send_registration_confirmation(user)
        except Exception:
            user.delete()
            return HttpResponse(False)
    except Exception:
        return HttpResponse(False)
    return HttpResponse(True)


def send_registration_confirmation(user):
    token = default_token_generator.make_token(user)
    title = "Curri email confirmation"
    content = "localhost/" + token
    send_mail(title, content, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def activationview(request):
    pass


def checkusername(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'username' in p.keys():
            name = p['username']
            return HttpResponse(user_util.username_valid(name))
    return HttpResponse('Invalid request')


def checkemail(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'email' in p.keys():
            email = p['email']
            return HttpResponse(user_util.email_valid(email))
    return HttpResponse('Invalid request')
