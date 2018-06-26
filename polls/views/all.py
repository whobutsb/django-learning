from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F
from django.contrib.auth import get_user_model

from ..models import Question, Choice
# Create your views here.

def index(request):
    questions = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

    return render(request, 'polls/index.html', {
        "latest_question_list": questions,
    })

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay question form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # F prevents race conditions and does the update on the database rather
        # than having python update and save the value
        # https://docs.djangoproject.com/en/2.0/ref/models/expressions/#avoiding-race-conditions-using-f
        selected_choice.votes = F('votes')  + 1
        selected_choice.save()
        # always return a HttpResponseRedirect after success POST data
        # this prevents the data from being posted twice if the user hits back

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
