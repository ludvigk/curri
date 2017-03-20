from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import Subject, Profile, SubjectUser, Lecture, Rating
from django.contrib.auth import logout
import json


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home/home.html', {'subjects': Subject.objects.filter(profile__user=request.user)})


@login_required(login_url='/accounts/login/')
def subject(request, subjectID):
    if not subjectID:
        return HttpResponse('')
    subject = Subject.objects.filter(subjectID=subjectID).first()
    if not subject:
        return HttpResponse('No such subject')
    return render(request, 'home/subject.html', {'subject':subject})


@login_required(login_url='/accounts/login/')
def add_subject(request, subjectID):
    user = request.user
    subject = Subject.objects.filter(subjectID=subjectID).first()
    try:
        profile = Profile.objects.get(user=user)
    except:
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
def delete_subject(request, subjectID):
    subject = Subject.objects.filter(subjectID=subjectID)
    if is_admin(request, subjectID):
        subject.delete()
        return HttpResponse("Delete successful")
    return HttpResponse("No permission")


@login_required(login_url='/accounts/login/')
def rate_lecture(request):
    if not request.method == 'POST':
        return HttpResponse('0')
    lectureID = request.POST.get('lectureID', '')
    score = request.nse(request.body)
    return HttpResponse(request.POST)
    lecture = Lecture.objects.get(id=int(lectureID))
    user = request.user
    #profile = Profile.objects.filter(user=user).first()
    #rating = lecture.rating.objects.filter(user=user)
    #if rating:
    #    return 0
    #rating.rating = score
    return HttpResponse("test")


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
def add_lecture(request, subjectID):
    if is_admin(request, subjectID):
        subject = Subject.objects.filter(subjectID=subjectID).first()
        Lecture.objects.create(subject=subject)
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def edit_lecture(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def remove_lecture(request):
    return HttpResponse('')


def is_admin(request, subjectID):
    try:
        user = request.user
        profile = Profile.objects.filter(user=user)
        subject = Subject.objects.filter(subjectID=subjectID).first()
        su = SubjectUser.objects.filter(user=profile, subject=subject).first()
        if su.permissions == "admin":
            return True
    except Exception as e:
        return False
    return False
