from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Vote

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
       return Question.objects.order_by('-pub_date')[:5]

#def index(request, question_id):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list':latest_question_list}
    #return render(request, 'polls/index.html', context)



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question':question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question':question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        question.add_geo_tag(request.request.META['REMOTE_ADDR'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"Selecciona una respuesta",
            })
    if Vote.objects.filter(choice=choice,voter=request.user).exists():
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"No se puede votar dos veces en una misma pregunta",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        Vote.objects.create(voter=request.user, choice=choice, geo_location=request.META['REMOTE_ADDR'])
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # In order to avoid race condition, use F()

   