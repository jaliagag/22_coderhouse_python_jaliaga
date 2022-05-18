#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1
# 1,1
#for i in range(50):
#    if i % 2 != 0:
#        if i % 3 == 0:
# 1,2            
#for i in range(3,50,6):
#            print(i)
# 2

#list = [21,33,-25,85,-3.6,27]
#num = list[0] 
#
#for i in list:
#    if i < num:
#        num = i
#print(f'el número menor es {num} y su índice es {list.index(num)}')

# 3

#persona = {'id':'','age':'','name':'','height':''}
#
#for i in persona:
#    a = input(f'What is your {i.upper()}? ')
#    persona[i] = a
#
#    #print(persona.values())
#
#print(persona)

# 4

b = 0

while b == 0:
    a = int(input("ingrese un número y veremos si es primo o no! "))
#for a in range(101):
    if a % 2 == 0:
        continue
    elif a % 3 == 0:
        continue
    elif a % 5 == 0:
        continue
    else:
        print(f'{a} es un número primo!')
        b = 1
    
