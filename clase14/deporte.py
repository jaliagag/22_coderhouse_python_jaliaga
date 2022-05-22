#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ciclista:
    def __init__(self,estilo,patrocinador):
        self.estilo = estilo
        self.patrocinador = patrocinador
    def hacerBici(self):
        print("estoy andando en bici")
    def __str__(self):
        print(f'soy un clicista de {self.estilo}')


class Corredor:
    def __init__(self,metros,estilo):
        self.metros = metros 
        self.estilo = estilo
    def correr(self):
        print('estoy corriendo!')
    def __str__(self):
        return f"soy un nadador de {self.estilo}"

class Nadador:
    def __init__(self,estilo):
        self.estilo = estilo
    def correr(self):
        print("nadando")
    def __str__(self):
        return f"soy un nadador de {self.estilo}"

class Triatleta(Nadador,Corredor,Ciclista):
    def __init__(self,estiloN,patrocinador,metros,tipo,estiloC,nombreYApellido,edad):
        # super no funcionaría porque es una herencia de múltiple clases
        Nadador.__init__(self,estiloN,patrocinador)
        Corredor.__init__(self,metros,tipo)
        Ciclista.__init__(self,estiloC)

        self.nombreYApellido = nombreYApellido
        self.edad = edad

    def __str__(self):
        return Nadador.__str__(self) + "\n" + Corredor.__str__(self) + "\n" + Ciclista.__str__(self) + "\n" + f"ni nombre es {self.nombreYApellido} y tengo {self.edad} años"
