#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = [1,2,3,4,5]
for valor in lista:
    print("soy un item de la lista y valgo", valor)
    valor *= 5
    print("soy un item de la lista y ahora valgo", valor)

indice = 0
num = [0,1,2,3,4,5,6,7,8,9,10]
for numero in num:
    num[indice] *= 5
    indice +=1
print(num)
