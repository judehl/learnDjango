from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.urls import reverse
from django.views import generic


def new_index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)


"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # 按pub_date倒序取前5条
    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {'question': question})
"""


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': "you didn't select a choice!"
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        # return HttpResponseRedirect('/polls/{qid}/results'.format(qid=question_id))
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
