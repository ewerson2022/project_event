from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *
from django.template import loader

def teste(request):
    return HttpResponse('testando...')


def exibir_evento(request):
    evento = Eventos
    return render(request= request, context={"evento": evento},template_name="agenda/exibir_evento.html")