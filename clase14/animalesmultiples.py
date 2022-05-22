#!/usr/bin/env python
# -*- coding: utf-8 -*-

# crear una herramienta múltiple, trabajando con mamífero, cetáceo, animalmarino

class Mamifero:
    def __init__(self, cantMamas, esperanzaDeVida):
        self.cantMamas = cantMamas
        self.__esperanzaDeVida = esperanzaDeVida
    def mamar():
        print('irene,yo y mi otro yo')
    def nacer():
        print('canción del rey león')

class AnimalMarino:
    def __init__(self,tieneBranqueas,especie):
        self.__tieneBranqueas = tieneBranqueas
        self.__especie = especie
    def nadar():
        print('nada bajo el marrrrr')

class Cetaceo(Mamifero,AnimalMarino):
    def __init__(self,cantMamas,esperanzaDeVida,tieneBranqueas,especie,notas,viveEn,peso):
        Mamifero.__init__(self,cantMamas,esperanzaDeVida)
        AnimalMarino.__init__(self,tieneBranqueas,especie)

        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso


orca = Cetaceo(0,150,'no','orca','altas','fondo del mar','6000')
#cachalote = Cetaceo()



print(orca.especie())
