from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home/base.html')


@login_required(login_url='/accounts/login/')
def subject(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def add_subject(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def create_subject(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def rate_lecture(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def rate_tag(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def add_tag(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def remove_tag(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def add_lecture(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def edit_lecture(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def remove_lecture(request):
    return HttpResponse('')
