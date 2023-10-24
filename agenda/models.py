from django.db import models

class Evento:
    def __init__(self, nome, categoria, local = None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link   

aula_python = Evento("aula de python", "backend", "rio de janeiro")
aula_js = Evento("aula de java script", "fullstack", link= "https://tamarcado.com/")

Eventos = [
    aula_python,
    aula_js,
]