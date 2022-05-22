#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pato:
    def hablar(self):
        print('cuac')

class Gato:
    def hablar(self):
        print('miau')

class Perro:
    def hablar(self):
        print('guau')


p = Pato()
g = Gato()
d = Perro()

def llamar_hablar(x):
    x.hablar()
l = [p,g,d]
for i in l:
    llamar_hablar(i)
