#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
import datetime

# funciones de la view

def saludo(request):
    return HttpResponse('Hola mundo')

def segunda_vista(request):
    return HttpResponse('<h1>Hola mundo</h1>')

def dia_de_hoy(request):
    dia = datetime.datetime.now()

    texto = f'hoy es día: <br>', dia

    return HttpResponse(texto)

def mi_nombre_es(self,nombre):
    texto = f'mi nombre es: ', nombre

    return HttpResponse(texto)

