#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# print(sys.argv)

def value(b):
    if int(b) > -1 and int(b) < 11:
        return True
    else:
        return False

if len(sys.argv) == 3 and (value(sys.argv[1]) and value(sys.argv[2])):
    nota1 = int(sys.argv[1])
    nota2 = int(sys.argv[2])
    if nota1 >= 7 and nota2 >= 7:
        print('Promocionado')
    elif nota1 >= 4 and nota2 >= 4:
        print('Aprobado, debe rendir final')
    elif nota1 <= 3 and nota2 >= 4:
        print('Desaprobado, debe rendir el primer parcial')
    elif nota2 <= 3 and nota1 >= 4:
        print('Desaprobado, debe rendir el segundo parcial')
    else:
        print('Desaprobó ambos parciales, debe recursar')
else:
    print('Error: uso correcto python ejercicio.py <nota 1er examen> <nota segundo examen>; ambos valores deben ser menores a 11')
