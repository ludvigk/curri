from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def index(request):
    return response('mysite/index.html')
