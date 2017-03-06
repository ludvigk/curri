from django.db import models
from django.utils import timezone


class Subject(models.Model):
    title = models.CharField(max_length=200)
    subjectCode = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_date', )


class SubjectUser(models.Model):
    user = models.ForeignKey('Profile')
    subject = models.ForeignKey('Subject')
    permissions = models.CharField(max_length=20)


class Tag(models.Model):
    creator = models.ForeignKey('auth.User')
    subject = models.ForeignKey('Subject', null=True)
    title = models.CharField(max_length=20)


class Lecture(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Subject', through='SubjectUser')
