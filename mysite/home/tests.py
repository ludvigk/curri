from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from accounts.models import *
from django.urls import reverse
from django.test import Client
from django.contrib import auth


# --- Test for views.py ---
#
# What has been tested?
# - create_subject
#
# What has not been tested?
# - home
# - subject, add_subject, delete_subject, rate_lecture
# - add_tag, rate_tag, remove_tag
# - add_lecture, edit_lecture, remove_lecture
# - statistics, is_admin

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


class DeleteSubjectTest(TestCase):
	def setUp(self):
		print("hei")
	def test_delete_subject(self):
		print("hei")


# uferdig
class AddLectureTest(TestCase):
	def setUp(self):
		self.client = Client()
		User.objects.create_user(username='testuser', password='bar')
		self.login_response = self.client.post(reverse('login'),
            {"loginusername": "testuser", "loginpassword": "bar"},
            follow=True)
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})

	def test_add_lecture(self):
		print("hei")


# uferdig
class IsAdminTest(TestCase):
	def setUp(self):
		self.client = Client()
		User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
            {"loginusername": "testuser", "loginpassword": "bar"},
            follow=True)
		self.subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})


	def test_is_admin(self):
		from home.views import is_admin
		subjectID = Subject.objects.first().subjectID
		self.assertTrue(is_admin(User.objects.first(), subjectID))

		#print(is_admin_response.content)