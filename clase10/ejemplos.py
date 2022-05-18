#!/usr/bin/env python
# -*- coding: utf-8 -*-

# funciona
#def resta(a=20,b=15):
def resta(a=None,b=None):
    if a == None or b == None:
        print("Error")
        return
    print(a - b)
    return a - b

print("1) resta(2,5)")
resta(2,5)

a = 10
def valor(param):
    return param * 10

print("2) paso por valor ")
print(valor(a))
print(a)

print("3) paso por referencia: cambia el estado de la lista fuera de la función")
b = [10,20,30,40]
print(f'valor inicial {b}')
def referencia(param):
    for i in range(len(param)):
        param[i] *= 10
        #param[i] *= 10
        #param[i] * 10

referencia(b)
print(f'valor final {b}')

print('4) evitar 3')

c = [10,20,30,40]
print(f'valor inicial {c}')
def no_mod(param):
    for i in range(len(param)):
        param[i] *= 10

no_mod(c[:])
print(f'valor final {c}')

# *args - tupla
print('5) *args - Q de argumentos indefinido')
def muchos_args(*args):
    s = 0
    for i in args:
        s += i
    return s

print(muchos_args(10,20,30,40))

# **kwargs - para diccionarios y jsons
print('6) **kwargs - para diccionarios y jsons')
def le_kwargs(**kwargs):
    s = 0
    for key,value in kwargs.items():
        print(key,'=',value)
        s += value
    return s

print(le_kwargs(a=10,b=29,c=50))

# recursividad
print('7) recursividad')
def recursividad(numero):
    numero -= 1
    if numero > 0:
        print(f'---->{numero}')
        recursividad(numero)
    else:
        print('boom!')

recursividad(5)

        







