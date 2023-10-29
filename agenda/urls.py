
from django.urls import path,include
from agenda.views import listar_eventos, exibir_evento

urlpatterns = [
    
    path('',listar_eventos),
    path('evento',exibir_evento)
]