#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dividir(a,b):
    return a/b

try:
    one = int(input('ingrese un número: '))
    two = int(input('ingrese un número: '))
    print(dividir(one,two))
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except Exception as e:
    print('woops algo salió mal:',type(e).__name__)
