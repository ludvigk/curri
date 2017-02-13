from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    return render(request, 'login/index.html')
