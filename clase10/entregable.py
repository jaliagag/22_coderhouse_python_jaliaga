#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def area_rectangulo(width,length):
    return width*length

print(area_rectangulo(15,10))

def area_circulo(radius):
    return (radius**2)*math.pi

print(area_circulo(5))

def relacion(first,second):
    if first > second:
        return 1
    elif first < second:
        return -1
    else:
        return 0
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

def intermedio(first,second):
    return (first+second)/2

print(intermedio(-12,24))

def recortar(number,bottom,top):
    if number < bottom:
        return bottom
    elif number > top:
        return top
    else:
        return number

    
print(recortar(15,0,10))

pairs = []
odd = []
    
def separar(little_list):
    for i in little_list:
        if i % 2 == 0:
            pairs.append(i)
        else:
            odd.append(i)
    pairs.sort()
    odd.sort()

separar([6,5,2,1,7])
print(pairs)
print(odd)


