#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

ques = int(input('Ingrese un número: '))

for i in range(1, ques):
    fizz_buzz(i)
