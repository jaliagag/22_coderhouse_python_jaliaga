#!/usr/bin/env python
# -*- coding: utf-8 -*-

variable_test = 10
def test():
    variable_test = 155
    # este print le da prioridad a la variable dentro de la función antes que a la variable de afuera
    print(variable_test)

test()
# error - las variables creadas en una función NO EXISTEN fuera de la misma
#print(variable_test)
