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
# - add_tag, remove_tag
# - is_admin
#
# What has not been tested?
# - home
# - subject
# - edit_lecture
# - statistics

class HomeTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
			{"loginusername": "testuser", "loginpassword": "bar"},
			follow=True)

	def test_home(self):
		request = self.factory.get('/')
		request.user = self.user
		home_response = self.client.get(reverse('home'))

		self.assertEqual(home_response.status_code,200)


class SubjectTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='testuser', password='bar')
		login_response = self.client.post(reverse('login'),
			{"loginusername": "testuser", "loginpassword": "bar"},
			follow=True)
		subject_response = self.client.get(reverse('create_subject'),
			{"subject": "test1", "subjectCode": "ABC1234"})
		#samme greia. Mulig opprett objekter

	def test_home(self):
		request = self.factory.get('/')
		request.user = self.user
		subject_response = self.client.get('/home/subject/'+Subject.objects.first().subjectID+'/')

		self.assertEqual(subject_response.status_code,200)


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


class EditLectureTest(TestCase):
	def setUp(self):
		pass

	def test_edit_lecture(self):
		pass


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


class AddTagTest(TestCase):
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
		

	def add_tag_test(self):
		tag_response = self.client.post(reverse('add_tag'),
			{"lectureID": Lecture.objects.first().id, "title": "test"})

		self.assertEqual(Tag.objects.first().title,"test")
		self.assertEqual(Tag.objects.first().lecture.subject.title,"test1")


class RateTagTest(TestCase):
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
		tag_response = self.client.post(reverse('add_tag'),
			{"lectureID": Lecture.objects.first().id, "title": "test"})

	def rate_tag_test(self):
		rate_response = self.client.post(reverse('rate_tag'),
			{"tagID": Tag.objects.first().id, "score": 3})

		self.assertEqual(TagRating.objects.first().rating, 3)
		

class RemoveTagTest(TestCase):
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
		tag_response = self.client.post(reverse('add_tag'),
			{"lectureID": Lecture.objects.first().id, "title": "test"})
		

	def remove_tag_test(self):
		pass


class StatisticsTest(TestCase):
	def setUp(self):
		pass

	def test_statistics(self):
		pass


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
