#!/usr/bin/env python
# -*- coding: utf-8 -*-

def par_impar(num):
    if int(num) % 2 == 0:
        return print(f"{num} es par")
    else:
        return print(f"{num} es impar")

#ques = input("Ingrese un número ")
print('Ingrese 0 para salir')

while ( ques := input('Ingrese un número: ') ) != '0':
    #if type(ques) == int:
    if ques.isdigit():
        par_impar(ques)
    else:
        print(f"{ques} no es un número honey ")

    #ques = input("Ingrese un número ")

    # exit
    if ques == "0":
        print("Bye!")
        break
