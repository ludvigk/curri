from django.test import TestCase
from . import models

# Create your tests here.

class TagInSubjectTestCase (TestCase)
	def setUp(self):
		Subject.objects.create(title = "Objektorientert Programmering", subjectCode = "TDT4100", subjectID="545454")
		Subject.objects.create(title = "Brukerkurs", subjectCode = "MA0001", subjectID = "220022")
		Subject.objects.create(title = "Programvareutvikling", subjectCode = "TDT4140", subjectID = "123123")
		Tag.objects.create(title = "Pekka", subject = Subject.objects.get(subjectID = "123123")  )

	def test_tag_in_subject(self):
		subject_title = Subject.objects.get(subjectID="123123").title
		subjectfromtag_title = Tag.objects.get(title="Pekka").subject.title
		self.assertEqual(subject_title,subjectfromtag_title)