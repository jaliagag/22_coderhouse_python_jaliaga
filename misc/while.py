#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = 5

while num > 0:
    print(f"{num}")
    num -= 1
print("terminó el conteo!")

change = 1

while change <= 3:
    txt = input("Escribe SI: ")
    if txt == "SI":
        print("ok, lo conseguiste en el intento", change)
        break
    change += 1
else:
    print("has agotado tus tres intentos")
