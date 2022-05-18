#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumar(n1,n2):
    return n1 + n2
def restar(n1,n2):
    return n1 - n2

fuera = 0

while True:
    if fuera == 0:
        a = float(input('Ingrese número inicial: '))
        c = float(input('Qué operación? 1) sumar 2) restar: '))
        b = float(input('Monto: '))
        if c == 1:
            print(sumar(a,b))
            fuera = sumar(a,b)
        elif c == 2:
            print(restar(a,b))
            fuera = restar(a,b)
        elif c == 0:
            break
    else:
        a = fuera
        c = float(input('Qué operación? 1) sumar 2) restar: '))
        b = float(input('Monto: '))
        if c == 1:
            print(sumar(a,b))
            fuera = sumar(a,b)
        elif c == 2:
            print(restar(a,b))
            fuera = restar(a,b)
        elif c == 0:
            break



    


    
