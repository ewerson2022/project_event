from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import Evento, Categoria         
from django.template import loader
import re

def listar_eventos(request):
    
     eventos = Evento.objects.all()
     return render(request = request, 
                   context={"eventos": eventos},
                   template_name ="agenda/listar_evento.html")
   

def exibir_evento(request):
    evento = {"nome": "teste",}
    return render(request= request, context={"evento": evento},template_name="agenda/exibir_evento.html")