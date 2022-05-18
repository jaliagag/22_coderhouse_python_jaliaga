#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Persona:
    # atributos de clase
    especie = "humano"
    pais = "Argentina"

    # constructor
    def __init__(self,nombre,edad,idn,mascota):
        # atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.idn = idn
        self.mascota = mascota

    # métodos
    # con parámetro
    def decir(self,speech): # parámetro
        print(f'{self.nombre} dice: {speech}')
    # sin parámetro
    def presentacion(self):
        #print(f'presentamos a {self.nombre} que tiene {self.edad} años y su DNI es {self.idn} y es de {self.pais}; su mascota es {self.mascota}')
        return 'presentamos a '+self.nombre+ 'que tiene '+self.edad+' años y su DNI es '+self.idn+' y es de '+self.pais+'; su mascota es '+self.mascota.__str__()

class Perro:
    def __init__(self,name,race):
        self.nombre = name
        self.raza = race
    def __str__(self):
        return f'{self.nombre}, {self.raza}'

class Gato:
    def __init__(self,name,race):
        self.nombre = name
        self.raza = race
    def __str__(self):
        return f'{self.nombre}, {self.raza}'

obama = Perro('obama','labrador negro')
simba = Gato('simba','calle')

paula = Persona('Paula', '32', '123456789',simba)
paula.decir('tengo un gato!') # argumento
print(paula.presentacion())

jose = Persona('Jose','33','987654321',obama)
jose.decir(f'vivo con el gato de {paula.nombre}!')
print(jose.presentacion())








