import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns FAlse for questions whose pub_date
        is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questoin whose pub_date is
        older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, minutes=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    """
    create a question with the given question_text and published the given
    number of days offset to now negative for questions published in the past
    positive for questions that have yet to be published
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        if no questions exist, message is displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        questions with a pub_date in the past are displayed on the index page.
        """
        create_question(question_text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question>']
        )

    def test_future_question(self):
        """
        questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")

class QuestionDetailsViewTests(TestCase):

    def test_future_question(self):
        """
        the detail view of a question with a pub_date in the future returns 404
        """
        future_question = create_question(question_text='Future question', days=4)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url);
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """ 
        the detail view of a question with a pub_date in the past displays
        the question text
        """
        past_question = create_question(question_text='Past question', days=-30)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url);
        self.assertContains(response, "Past question")
