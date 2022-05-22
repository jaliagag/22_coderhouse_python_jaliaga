#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(numero):
    if numero > 1:
        numero *= factorial(numero-1)
    return numero

#print(factorial(5))

#a = 0
#b = 1
#
#c = 0
#
#while b < 100000000:
#    c = a + b
#    a = b
#    b = c
#    print(b)

#def fibo(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        a = n - 1
#        b = n - 2
#        #print('a: ', a)
#        #print('b: ', b)
#        return fibo(a) + fibo(b)
#    #return c
#
#for i in range(8):
#    print(fibo(i))
    

