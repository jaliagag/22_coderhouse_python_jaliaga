#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = [12,24,36,47]
def doblar_valor(algo):
    for i,n in enumerate(algo):
        #print(f'posición: {i}')
        print(f'numero: {n*2}')

#doblar_valor(lista)

def factorial(numero):
    print(numero)
    if numero > 1:
        numero = numero * factorial(numero-1)
        print(numero)
    return numero

print(factorial(5))
