from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import Subject, Profile, SubjectUser
from django.contrib.auth import logout
from accounts.models import Subject, Profile


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home/home.html', {'subjects': Subject.objects.filter(profile__user=request.user)})


@login_required(login_url='/accounts/login/')
def subject(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def add_subject(request):
    user = request.user
    subject = request.subject
    profile = Profile.objects.create(user=user)
    profile.save()
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def create_subject(request):
    user = request.user
    p = request.GET.copy()
    subject = p.get('subject', '')
    subjectCode = p.get('subject_code', '')
    subject = Subject.objects.create(title=subject,
                                              subjectCode=subjectCode
                                              )
    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = Profile.objects.create(user=user)
    SubjectUser.objects.create(user=profile, subject=subject, permissions='admin')
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
