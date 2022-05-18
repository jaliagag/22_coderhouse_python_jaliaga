#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Atleta:

    def __init__(self, name, lastname, height, weight, phone): # definimos los datos como datos públicos
        self.__name = name # al pnoer __ lo hacemos privado; lo mejor es hacer que todo primero sea privado y después lo abrimos
        self.__lastname = lastname
        self.__height = height
        self.__weight = weight
        self.__phone = phone # dato privado
        self.__imc = weight / (height * height)

    def getNameLastname(self):
        return self.__name, self.__lastname
    def getHeightWeight(self):
        return self.__height, self.__weight
    def getPhone(self):
        return self.__phone
    def getImc(self):
        return self.__imc

    def setImc(self):
        self.__imc = self.__weight/(self.__height ** 2)
    def setWeight(self, w):
        self.__weight = w
        self.setImc()

    def setHeight(self, h):
        self.__height = h
        self.setImc()



messi = Atleta('lionel','messi',1.69, 70, "3513022380")

print(messi.getImc())

messi.setWeight(94)
#messi.setImc()
print(messi.getImc())


