#Django Import

from django.test import TestCase
from .models import Question


class QuestionModelTest(TestCase):
	"""Fot testing the logic that we have implemented in the model classes
	"""
	def test_dummy_function_bool_invert(self):
		q = Question()
		self.assertIs(q.dummy_function_return_invert(1),False)

	def test_dummy_function_string_invert(self):
		q=Question()
		self.assertIs(q.dummy_function_return_invert(parm='hello'),False)