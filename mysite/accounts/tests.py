from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from accounts.models import *
from django.urls import reverse
from django.test import Client
from django.contrib import auth

# Create your tests here.


# --- Test for models.py ---
#
# What has been tested?
# - Subject, Tag, SubjectUser, Profile
#
# What has not been tested?
# - ***DONE***


class SubjectTestCase(TestCase):
    def setUp(self):
        Subject.objects.create(title="sub1", subjectCode='1', subjectID="000001")
        Subject.objects.create(title="sub2", subjectCode='2', subjectID="000002")

    def test_subject_success(self):
        subject1 = Subject.objects.get(title="sub1")
        subject2 = Subject.objects.get(title="sub2")
        self.assertIs(subject1 == subject2, False)


class TagInSubjectTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='foo', email='testest@notadomain.not', password='bar')

        Subject.objects.create(
            title="Objektorientert Programmering",
            subjectCode="TDT4100",
            subjectID="545454")

        Subject.objects.create(
            title="Brukerkurs",
            subjectCode="MA0001",
            subjectID="220022")

        Subject.objects.create(
            title="Programvareutvikling",
            subjectCode="TDT4140",
            subjectID="123123")

        Profile.objects.create(user=self.user)

        Lecture.objects.create(
            title="Best lecture ever!",
            subject=Subject.objects.get(
                subjectID="123123"))


    def test_tag_in_subject(self):
        Tag.objects.create(
            title="Intro",
            lecture=Lecture.objects.first(),
            creator=self.user)

        lecture_title = Lecture.objects.get(subject=Subject.objects.get(subjectID="123123")).title
        lecturefromtag_title = Tag.objects.get(title="Intro").lecture.title
        self.assertEqual(lecture_title, lecturefromtag_title)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='foo', email='testest@notadomain.not', password='bar')
        Subject.objects.create(title="sub1", subjectCode='1', subjectID="000001")
        Subject.objects.create(title="sub2", subjectCode='2', subjectID="000002")

    def test_profile(self):
        # Create subjects
        s3 = Subject(title="sub3", subjectCode='3', subjectID="000003")
        s3.save()
        s4 = Subject(title="sub4", subjectCode='4', subjectID="000004")
        s4.save()

        # Create profile
        p1 = Profile.objects.create(user=self.user)
        p1.save()

        # Relate profile ("user") to subject
        SubjectUser.objects.create(user=p1, subject=s3)
        SubjectUser.objects.create(user=p1, subject=s4)

        # Delete the first subject added.
        p1.subjects.filter(title="sub3").delete()


class LectureTestCase(TestCase):
    def setUp(self):
        s3 = Subject(title="sub3", subjectCode='3', subjectID="000003")
        s3.save()
        s4 = Subject(title="sub4", subjectCode='4', subjectID="000004")
        s4.save()

    def test_lecture(self):
        Lecture.objects.create(
            title="Best lecture ever!",
            subject=Subject.objects.get(
                subjectID="000003"))


class DuplicateSubjectTestCase(TestCase):
    def setUp(self):
        Subject.objects.create(title="sub1", subjectCode='1', subjectID="000001")

    def test_create_duplicate(self):
        try:
            Subject.objects.create(title="sub2", subjectCode='2', subjectID="000001")
        except BaseException:
            print("Cannot create subject with duplicate ID")
        finally:
            print("Dette skjer")

# --- end of models.py tests ---


# --- Test for views.py ---
#
# What has been tested?
# -
#
# What has not been tested?
# - login, register, send_registration_confirmation
# - activationview
# - checkusername, checkemail
# - change_password

class LoginPageGetTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='foo', password='bar')

    def test_login(self):

        # Måten vi MÅ få det til å funke på:
        
        response = self.client.post(reverse('login'),
                    {"loginusername":"foo","loginpassword":"bar"}, 
                    follow = True)

        self.assertEqual(response.context['user'].is_authenticated(),True)


class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        response=self.client.post(reverse('register'),{"username":"foofoo123123","email":"exburn0@gmail.com","password":"barbar123123"},follow=True)
        
        from django.contrib.auth import get_user_model
        user_model = get_user_model()
        user = user_model.objects.get(username = "foofoo123123")
        user.is_active = True
        self.client.post(reverse('login'),
            {"loginusername":"foofoo123123","loginpassword":"barbar123123"}, 
            follow = True)
        self.assertEqual(response.context['user'].is_authenticated(),True)


class CheckUsernameTest(TestCase):
    def SetUp(self):
        self.client = Client()

    def test_checkusername(self):
        User.objects.create_user(username='123123', password='bar')

        response = self.client.get(reverse('checkusername'),{"username" : "123123"})
        response2 = self.client.get(reverse('checkusername'),{"username" : "unique"})

        # Denne skal ikke være invalid.. hmm
        self.assertContains(response, "False")
        self.assertContains(response2, "True")