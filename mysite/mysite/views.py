from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'mysite/index.html')
