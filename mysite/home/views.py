from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import Subject, Profile, SubjectUser, Lecture, Rating, Tag
from django.contrib.auth import logout
import json
from django.db.models import Prefetch


@login_required(login_url='/accounts/login/')
def home(request):
    queryset = SubjectUser.objects.filter(user__user=request.user)
    pf = Prefetch("subjectuser_set", queryset=queryset, to_attr="su")
    subjects = Subject.objects.filter(profile__user=request.user).prefetch_related(pf)
    return render(request, 'home/home.html', {'subjects': subjects})


@login_required(login_url='/accounts/login/')
def subject(request, subjectID):
    if not subjectID:
        return HttpResponse('')
    profile = Profile.objects.filter(user=request.user).first()
    queryset = SubjectUser.objects.filter(user__user=request.user)
    pf = Prefetch("subjectuser_set", queryset=queryset, to_attr="su")
    subject = Subject.objects.filter(profile__user=request.user).prefetch_related(pf).get(subjectID=subjectID)
    if not subject:
        return HttpResponse('No such subject')
    return render(request, 'home/subject.html', {'subject': subject})


@login_required(login_url='/accounts/login/')
def add_subject(request):
    user = request.user
    try:
        subjectID = request.POST.get('subjectID', '')
        subject = Subject.objects.filter(subjectID=subjectID).first()
    except Exception as e:
        return HttpResponse('No such subject')
    try:
        profile = Profile.objects.get(user=user)
    except Exception as e:
        profile = Profile.objects.create(user=user)
    finally:
        if not subject:
            return HttpResponse('')
        SubjectUser.objects.get_or_create(user=profile, subject=subject, permissions='student')
        return HttpResponse('')


@login_required(login_url='/accounts/login/')
def create_subject(request):
    user = request.user
    p = request.GET.copy()
    subject = p.get('subject', '')
    subjectCode = p.get('subject_code', '')
    subject = Subject.objects.create(title=subject,
                                     subjectCode=subjectCode)
    try:
        profile = Profile.objects.get(user=user)
    except Exception as e:
        profile = Profile.objects.create(user=user)
    SubjectUser.objects.create(user=profile, subject=subject, permissions='admin')
    profile.save()
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def delete_subject(request, subjectID):
    subject = Subject.objects.filter(subjectID=subjectID)
    if is_admin(request, subjectID):
        subject.delete()
        return redirect('home')
    return HttpResponse("No permission")


@login_required(login_url='/accounts/login/')
def rate_lecture(request):
    if not request.method == 'POST':
        return HttpResponse('0')
    lectureID = request.POST.get('lectureID', '')
    score = request.POST.get('score', '')
    lecture = Lecture.objects.get(id=int(lectureID))
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    try:
        rating = lecture.rating.objects.filter(user=user)
        return ('False')
    except Exception as e:
        rating = Rating.objects.create(user=profile, rating=int(score), lecture=lecture)
        return HttpResponse('True')


@login_required(login_url='/accounts/login/')
def rate_tag(request):
    if not request.method == 'POST':
        return HttpResponse('0')
    tagID = request.POST.get('tagID', '')
    score = request.POST.get('score', '')
    tag = Tag.objects.get(id=int(tagID))
    user = request.user
    profile = Profile.objects.get(user=user)
    try:
        rating = lecture.rating.objects.filter(user=user)
        return ('False')
    except Exception as e:
        rating = TagRating.objects.create(user=profile, rating=int(score), tag=tag)
        return HttpResponse('True')


@login_required(login_url='/accounts/login/')
def add_tag(request):
    lectureID = int(request.POST.get('lectureID', ''))
    lecture = Lecture.objects.get(id=lectureID)
    title = request.POST.get('title','')
    tag = Tag.objects.get_or_create(creator=request.user, lecture=lecture, title=title)
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def remove_tag(request):
    if is_admin(request, subjectID):
        pass
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def add_lecture(request, subjectID):
    if is_admin(request, subjectID):
        subject = Subject.objects.filter(subjectID=subjectID).first()
        Lecture.objects.create(subject=subject)
    return redirect('subject', subjectID)


@login_required(login_url='/accounts/login/')
def edit_lecture(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def remove_lecture(request, subjectID):
    if is_admin(request, subjectID):
        lecture = Lecture.objects.get(id=lectureID)
        lecture.delete()
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def statistics(request):
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
