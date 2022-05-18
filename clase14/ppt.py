#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad

    # método genérico pero con implementación particular
    def hablar(self):
        # método vacío
        pass

    # método genérico pero con implementación particular
    def moverse(self):
        pass

    def describeme(self):
        print('soy un animal del tipo', type(self).__name__)

class Perro(Animal):
    def hablar(self):
        print('guau!')
    def moverse(self):
        print('moverse en 4 patas')

class Vaca(Animal):
    def hablar(self):
        print('muuuu')
    def moverse(self):
        print('moverse en 4 patas')

class Abeja(Animal):
    def hablar(self):
        print('bzzz')
    def moverse(self):
        print('volando')
    # nuevo método
    def picar(self):
        print('picar!')


mi_perro = Perro('mamifero',10)
mi_vaca = Vaca('mamifero',6)
mi_abeja = Abeja('insecto',1)

mi_perro.describeme()
mi_vaca.describeme()
mi_abeja.describeme()

mi_perro.hablar()
mi_vaca.hablar()
mi_abeja.hablar()

mi_perro.moverse()
mi_vaca.moverse()
mi_abeja.moverse()

mi_abeja.picar()




