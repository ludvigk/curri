from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from accounts.models import *

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
		Subject.objects.create(title = "sub1", subjectCode = '1', subjectID = "000001")
		Subject.objects.create(title = "sub2", subjectCode = '2', subjectID = "000002")

	def test_subject_success(self):
		subject1 = Subject.objects.get(title="sub1")
		subject2 = Subject.objects.get(title="sub2")
		self.assertIs(subject1==subject2,False)


class TagInSubjectTestCase(TestCase):
	def setUp(self):


		self.user = User.objects.create_user(username='foo', email='testest@notadomain.not', password='bar')


		Subject.objects.create(title = "Objektorientert Programmering", subjectCode = "TDT4100", subjectID="545454")
		Subject.objects.create(title = "Brukerkurs", subjectCode = "MA0001", subjectID = "220022")
		Subject.objects.create(title = "Programvareutvikling", subjectCode = "TDT4140", subjectID = "123123")
		Tag.objects.create(title = "Intro", subject = Subject.objects.get(subjectID = "123123"),creator=self.user  )

	def test_tag_in_subject(self):
		subject_title = Subject.objects.get(subjectID="123123").title
		subjectfromtag_title = Tag.objects.get(title="Intro").subject.title
		self.assertEqual(subject_title,subjectfromtag_title)


class ProfileTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='foo', email='testest@notadomain.not', password='bar')
		Subject.objects.create(title = "sub1", subjectCode = '1', subjectID = "000001")
		Subject.objects.create(title = "sub2", subjectCode = '2', subjectID = "000002")


	def test_profile(self):
		#Create subjects
		s3 = Subject(title = "sub3", subjectCode = '3', subjectID = "000003")
		s3.save()
		s4 = Subject(title = "sub4", subjectCode = '4', subjectID = "000004")
		s4.save()

		#Create profile
		p1 = Profile.objects.create(user = self.user)
		p1.save()

		#Relate profile ("user") to subject
		SubjectUser.objects.create(user=p1,subject=s3)
		SubjectUser.objects.create(user=p1,subject=s4)

		#Delete the first subject added.
		p1.subjects.filter(title="sub3").delete()


class LectureTestCase(TestCase):
	def setUp(self):
		s3 = Subject(title = "sub3", subjectCode = '3', subjectID = "000003")
		s3.save()
		s4 = Subject(title = "sub4", subjectCode = '4', subjectID = "000004")
		s4.save()


	def test_lecture(self):
		Lecture.objects.create(title="Best lecture ever!", subject=Subject.objects.get(subjectID="000003"))


# --- Test for views.py ---
#
# What has been tested?
# - 
#
# What has not been tested?
# -