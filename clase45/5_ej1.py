#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = 0
value = 0
while n == 0:
    ques = int(input("Ingrese un número: "))
    if ques == 0:
        print("resultado final",value)
        n = 1
        break
    else:
        value += ques

