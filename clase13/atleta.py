#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Atleta:
    def __init__(self,name,lastname,height,weight,phone):
        self.name = name
        self.lastname = lastname
        self.__height = height
        self.__weight = weight
        self.__phone = phone
        self.__imc = weight / (height * height)

    def __str__(self):
        return f'{self.name}, {self.lastname}'

    def setImc(self):
        self.__imc = self.__weight / (self.__height * self.__height)
        
    def setHeight(self,h):
        self.__height = h
        self.setImc()
    def setWeight(self,w):
        self.__weight = w
        self.setImc()

    def getImc(self):
        return f'{self.__imc}'

print('Bienvenidos al menú de creación de atletas!')

while True:
    print('¿Qué desea hacer?')
    a = int(input('1) Crear atleta\n2) Modificar atleta\n3) Salir del menú\n'))
    if a == 3:
        break
    elif a == 1:
        name = input('Nombre del atleta: ')
        lastname = input('Apellido del atleta: ')
        height = float(input('Altura del atleta: '))
        weight = float(input('Peso del atleta: '))
        phone = input('Teléfono del atleta: ')

        # crear atleta
        atleta = Atleta(name,lastname,height,weight,phone)
        print(f'El IMC del atleta es {atleta.getImc()}')
    elif a == 2:
        pass
    else:
        print('Por favor, ingrese 1, 2 o 3')

#joe = Atleta('jose','aliaga',1.91,72,'3513022380')

#print(joe.getImc())
#joe.setWeight(90)
#print(joe.getImc())

