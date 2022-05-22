#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dividir(a,b):
    #return a/b
    if b == 0:
        return "B no puede ser 0!"
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a/b
    else:
        print('ingrese números solamente')
        return 

#dividir('a',2)
print(dividir(4,0))
print(dividir([2,3],4))
