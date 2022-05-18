#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://docs.google.com/presentation/d/1ZgusHtU13D7qxtCUtB4UFpTKkEFi-XC0/edit#slide=id.p1
# https://colab.research.google.com/drive/1Ud80qk0AaNI5mf5q3azQ2vtebxksfniR?usp=sharing

################################################
#try:
#    n = int(input('ingresar un número: '))
#    m = 4
#    print(f'{n}/{m}={n/m}')
#except:
#    print('algo salió mal')
#

################################################
#def dividir(num,div):
#    return num/div
##a = int(input("ingrese un número: "))
##b = int(input("ingrese un número: "))
##print(dividir(a,b))
#
#try:
#    a = int(input("ingrese un número: "))
#    b = int(input("ingrese un número: "))
#    print(dividir(a,b))
#except ZeroDivisionError:
#    print('mannnn no se puede dividir por 0!')
#except ValueError: 
#    print('solo números bruh!')
#except:
#     print('woops algo salió mal')   

################################################
#while(True):
#    try: # ejecuta esto
#        n = float(input("introduce un número: "))
#        m = 4
#        print(f'{n}/{m}={n/m}')
#    except: # ejecuta esto si hay errores
#        print('ha ocurrido un error - introduce un número')
#    else: # se ejecuta si el bloque try se ejecuta sin errores
#        print('se completó con éxito el programa')
#        break
#    finally: # se ejecuta siempre, error o no error
#        print('waruppppp')

################################################

try:
    n = int(input('introduce un número: '))
    5/n
except TypeError:
    print('no se puede dividir el número entre una cadena de caracteres')
except ValueError:
    print('debes introducir un número')
except ZeroDivisionError:
    print('no se puede dividir por 0!')
except Exception as e:
    print('Ha ocurrido un error =>',type(e).__name__)
# __name__ es un atributo especial de e
