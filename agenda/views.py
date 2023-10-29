from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from agenda.models import Evento, Categoria         
from django.template import loader
import re
from datetime import date
from django.urls import reverse


def listar_eventos(request):

        eventos = Evento.objects.filter(data__gte=date.today()) 
        #  eventos = Evento.objects.all()
        return render (request = request, 
                    context={"eventos": eventos},
                    template_name ="agenda/listar_evento.html",
                    )


def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id = id)
    return render(request = request, 
                   context={"evento": evento},
                   template_name ="agenda/exibir_evento.html")
                   
    