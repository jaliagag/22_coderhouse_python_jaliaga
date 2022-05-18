#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def hablar(self,b):
        print(f'{self.nombre} dice {b}')
