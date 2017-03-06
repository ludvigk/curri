from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from accounts.models import Subject, Profile


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home/base.html', {'subjects': Subject.objects.all()})


@login_required(login_url='/accounts/login/')
def subject(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def add_subject(request):
    user = request.user
    subject = request.subject
    profile = accounts.Profile.objects.create(user=user)
    profile.save()
    return HttpResponse('')


#@login_required(login_url='/accounts/login/')
def create_subject(request):
    return HttpResponse('Hello')
    user = request.user
    subject = accounts.Subject.objects.create(title=request.subject,
                                              subjectCode=request.subject_code
                                              )
    try:
        profile = accounts.Profile.objects.get(user=user)
    except:
        profile = accounts.Profile.objects.create(user=user)
    profile.subjects.add(subject)
    profile.save()
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