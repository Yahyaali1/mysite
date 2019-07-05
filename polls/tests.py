import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question
# Create your tests here.

def create_question(question_text,days):
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text,pub_date = time)

class QuestionIndexViewTests(TestCase):

	def test_no_question(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	def test_past_question(self):
		create_question('new Question', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: new Question>'])