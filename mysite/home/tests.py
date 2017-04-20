from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from accounts.models import *
from django.urls import reverse
from django.test import Client
from django.contrib import auth


# --- Test for views.py ---
#
# What has been tested?
# - create_subject, add_subject delete_subject
# - add_lecture, rate_lecture, remove_lecture
# - is_admin
#
# What has not been tested?
# - home
# - subject
# - add_tag, rate_tag, remove_tag
# - edit_lecture
# - statistics

class CreateSubjectTest(TestCase):
	def setUp(self):
		self.client = Client()
		User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
            {"loginusername": "testuser", "loginpassword": "bar"},
            follow=True)

	def test_create_subject(self):
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})
		self.assertEqual(Subject.objects.first().title,"test1")


class AddSubjectTest(TestCase):
	def setUp(self):
		Subject.objects.create(title="sub1", subjectCode='1', subjectID="000001")

		self.client = Client()
		User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
            {"loginusername": "testuser", "loginpassword": "bar"},
            follow=True)

	def test_add_subject(self):
		response = self.client.post(reverse('add_subject'),
			{"subjectID": "000001"})

		self.assertEqual(SubjectUser.objects.first().user.user.username,'testuser')




class DeleteSubjectTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
            {"loginusername": "testuser", "loginpassword": "bar"},
            follow=True)
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})

	def test_delete_subject(self):
		subjectID = Subject.objects.first().subjectID

		delete_response = self.client.get('/home/delete_subject/'+subjectID+'/')

		self.assertEqual(None,Subject.objects.first())


class AddLectureTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
			{"loginusername": "testuser", "loginpassword": "bar"},
			follow=True)
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})

	def test_add_lecture(self):
		lecture_response = self.client.post('/home/add_lecture/'+Subject.objects.first().subjectID+'/',
			{"title": "Forelesning 1"})

		self.assertEqual(Lecture.objects.first().title,"Forelesning 1")


class RemoveLectureTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
			{"loginusername": "testuser", "loginpassword": "bar"},
			follow=True)
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})
		lecture_response = self.client.post('/home/add_lecture/'+Subject.objects.first().subjectID+'/',
			{"title": "Forelesning 1"})

	def test_remove_lecture(self):
		remove_response = self.client.post('/home/remove_lecture/'+Subject.objects.first().subjectID+'/',
			{"lectureID": Lecture.objects.first().id})

		self.assertEqual(Lecture.objects.first(), None)



class RateLectureTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
			{"loginusername": "testuser", "loginpassword": "bar"},
			follow=True)
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})
		lecture_response = self.client.post('/home/add_lecture/'+Subject.objects.first().subjectID+'/',
			{"title": "Forelesning 1"})

	def test_rate_lecture(self):
		rate_response = self.client.post(reverse('rate_lecture'),
			{"lectureID": Lecture.objects.first().id,
			"score": 3})
		self.assertEqual(Rating.objects.first().rating, 3)

class IsAdminTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.client = Client()
		self.user = User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
		{"loginusername": "testuser", "loginpassword": "bar"},
			follow=True)
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})


	def test_is_admin(self):
		from home.views import is_admin
		request = self.factory.get('/')
		request.user = self.user
		subjectID = Subject.objects.first().subjectID
		self.assertTrue(is_admin(request, subjectID))