from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import *
from django.views.generic import ListView, DetailView
from common.views import TitleMixin


class IndexListView(TitleMixin, ListView):
    title = 'Questions'
    template_name = 'polls/index.html'
    model = Question
    context_object_name = 'questions'

    def get_queryset(self):
        queryset = Question.objects.order_by('-pub_date')
        return queryset


class DetailAnswerView(TitleMixin, DetailView):
    title = 'Details'
    template_name = 'polls/detail.html'
    model = Question


class ResultsView(TitleMixin, DetailView):
    title = 'Results'
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse('results', args=[question.id]))
