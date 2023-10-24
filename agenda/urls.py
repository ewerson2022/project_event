
from django.urls import path,include
from agenda.views import teste, exibir_evento

urlpatterns = [
    
    path('',teste),
    path('evento',exibir_evento)
]