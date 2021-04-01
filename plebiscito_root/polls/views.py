from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Plebiscito, coming soon...")

def detail(request, question_id):
    return HttpResponse("Pregunta %.s" % question_id)

def results(request, question_id):
    return HttpResponse("Resultados de la pregunta %s.")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voto realizado sobre la pregunta %s." % question_id)
