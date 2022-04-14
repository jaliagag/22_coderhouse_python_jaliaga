#!/usr/bin/env python
# -*- coding: utf-8 -*-

paises = ['Canada', 'USA', 'Australia', 'Argentina', 'China', 'India']

print("1) los países")
for i in paises:
    print(i)

par_sum=0
print("2) suma números pares")
for i in range(100):
    if i%2==0:
        par_sum += i
print(par_sum)

print("3) 1 al diez al revés")
for i in range(10,0,-1):
    print(i)

print("4) cantidad de números")
ques = input("Ingrese un número: ")
l = 0

for i in ques:
    l+=1
print("Tu número tiene", l, "números")
