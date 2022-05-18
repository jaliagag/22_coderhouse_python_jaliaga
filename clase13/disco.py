#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Perro:
  # atributo de clase - todos objetos van a tener estos atributos en común, no lo podemos modificar
  especie = "Mamífero"
  # el constructor
  def __init__(self,nombre,raza):
    # atributos de instancia
    self.nombre = nombre
    self.raza = raza
  def ladrar(self):
    print('guau!')
  def caminar(self, pasos):
    print(f'di {pasos} pasos')

##obama = Perro('Obama','Labrador')
##print(obama) # nos muestra el espacio del objeto en memoria
##print(f'mejor verlo atributo por atributo {obama.nombre}, {obama.raza}')

obama = Perro('Obama','Labrador')
obama.caminar(8)
obama.ladrar()


