from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import Subject, Profile, SubjectUser, Lecture, Rating, Tag, TagRating
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
    profile = Profile.objects.get(user=request.user)
    queryset = SubjectUser.objects.filter(user__user=request.user)
    queryset2 = Rating.objects.filter(user=profile)
    pf = Prefetch("subjectuser_set", queryset=queryset, to_attr="su")
    pf2 = Prefetch("lecture_set__rating_set", queryset=queryset2)
    subject = Subject.objects.filter(
        profile__user=request.user).prefetch_related(pf).filter(
            subjectID=subjectID).prefetch_related("lecture_set", pf2).first()
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
            return HttpResponse('No such subject')
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
    rating, created = TagRating.objects.get_or_create(user=profile, tag=tag)
    rating.rating = int(score)
    rating.save()
    return HttpResponse(rating.rating)


@login_required(login_url='/accounts/login/')
def add_tag(request):
    lectureID = int(request.POST.get('lectureID', ''))
    lecture = Lecture.objects.get(id=lectureID)
    title = request.POST.get('title','').lower()
    if not title or Tag.objects.filter(lecture=lecture, title=title):
        return HttpResponse('False')
    tag = Tag.objects.get_or_create(creator=request.user, lecture=lecture, title=title)
    return HttpResponse('True')


@login_required(login_url='/accounts/login/')
def remove_tag(request):
    if is_admin(request, subjectID):
        pass
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def add_lecture(request, subjectID):
    if is_admin(request, subjectID):
        title = request.POST.get('title', '')
        repeated = request.POST.get('repeatedOptions', '')
        date = request.POST.get('date', '')
        datelist = []
        enddatelist = []
        if date:
            datelist = date.split('/')
            date = '{}-{}-{}'.format(datelist[2], datelist[0], datelist[1])
        subject = Subject.objects.filter(subjectID=subjectID).first()
        if repeated:
            enddate = request.POST.get('enddate', '')
            if enddate:
                enddatelist = enddate.split('/')
                enddate = '{}-{}-{}'.format(enddatelist[2], enddatelist[0], enddatelist[1])
            else:
                enddate = date
            from datetime import date, timedelta
            sevendays = timedelta(days=7)
            d1 = date(int(datelist[2]), int(datelist[0]), int(datelist[1]))
            d2 = date(int(enddatelist[2]), int(enddatelist[0]), int(enddatelist[1]))
            while d1 <= d2:
                date = "{}-{}-{}".format(d1.year, d1.month, d1.day)
                Lecture.objects.create(subject=subject, title=title, date=date)
                d1 += sevendays
        else:
            if date:
                Lecture.objects.create(subject=subject, title=title, date=date)
            else:
                Lecture.objects.create(subject=subject, title=title)
    return redirect('subject', subjectID)


@login_required(login_url='/accounts/login/')
def edit_lecture(request):
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def remove_lecture(request, subjectID):
    if is_admin(request, subjectID):
        lectureID = request.POST.get('lectureID', '')
        lecture = Lecture.objects.get(id=lectureID)
        lecture.delete()
    return HttpResponse('')


@login_required(login_url='/accounts/login/')
def statistics(request, subjectID):
    from graphos.sources.model import SimpleDataSource
    from graphos.renderers.gchart import ColumnChart
    from django.db.models import Avg, Count
    subject = Subject.objects.get(subjectID=subjectID)
    lectures = Lecture.objects.filter(subject=subject).annotate()
    user = request.user
    profile = Profile.objects.get(user=user)
    rating = Rating.objects.filter(lecture__subject=subject).values('lecture_id').annotate(Avg('rating'))
    data = [list(rating[0].keys())]
    for el in rating:
        data_set = [Lecture.objects.get(id=el['lecture_id']).title, el['rating__avg']]
        data += [data_set]
    data_source = SimpleDataSource(data=data)
    chart = ColumnChart(data_source)
    return render(request, 'home/statistics.html', {'chart': chart})


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
