from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None or request.user.is_authenticated():
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html')

def register(request):
    username         = request.POST.get('username', '')
    email            = request.POST.get('email', '')
    password         = request.POST.get('password', '')
    confirm_password = request.POST.get('confirm-password', '')
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect('/accounts/login/')
