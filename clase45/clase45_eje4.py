#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = int(input("¿Cuántos números vas a introducir? "))
lista = []

for i in range (a):
    #b = int(input("ingrese un número: : "))
    lista.append(int(input("ingrese un número: ")))

suma = 0

print(lista)
print(len(lista))

for h in lista:
    suma += h

print("la media de los números introducidos es de", suma/len(lista))

