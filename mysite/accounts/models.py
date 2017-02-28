from django.db import models
from django.utils import timezone


class Subject(models.Model):
    title = models.CharField(max_length=200)
    subjectCode = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    admins = models.ManyToManyField('auth.User', through='SubjectAdmin')
    tags = models.ManyToManyField('Tag', through='SubjectTags')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_date', )


class SubjectAdmin(models.Model):
    admin = models.ForeignKey('auth.User')
    subject = models.ForeignKey('Subject')


class Tag(models.Model):
    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=20)


class SubjectTags(models.Model):
    tag = models.ForeignKey(Tag)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)


class Lecture(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
