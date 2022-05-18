#!/usr/bin/env python
# -*- coding: utf-8 -*-

# se usa cuando no sabemos la cantidad de iteraciones o elementos
num = 5
print("iniciamos la cuenta regresiva\n")

while num > 0:
    print(f"el num es:{num}")
    num -= 1

print("\nterminó la cuenta regresiva")

# while else
# entra si no se cumple la condición 

chance = 1
while change <= 3:
    txt = input("escribe si: ")
    if txt == "SI":
        print("Ok, lo conseguiste en el intento", chance)
        break # escapar de la iteración
    chance += 1
else:
    print("has agotado tus tres intentos")


