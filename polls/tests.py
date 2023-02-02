import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learn.settings')
import django

django.setup()

from django.test import TestCase
from django.urls import reverse
from .models import Question


class IndexListViewTestCase(TestCase):
    fixtures = ['choices.json', 'questions.json']

    def setUp(self):
        self.path = reverse('index')
        self.response = self.client.get(self.path)
        self.questions = Question.objects.all()

    def test_page_view(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'polls/index.html')
        self.assertEqual(self.response.context_data['title'], 'Questions')
        self.assertEqual(len(self.response.context_data['object_list']), len(self.questions))


class DetailAnswerViewTestCase(TestCase):

    def test_page_get(self):
        question = Question.objects.create(question_text='What`s new?')
        print(question)
        path = reverse('detail', kwargs={'pk': question.id})
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/detail.html')
        self.assertEqual(response.context_data['title'], 'Details')




