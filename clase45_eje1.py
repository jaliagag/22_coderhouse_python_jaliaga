#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("¿Qué operación quiere realizar?\n\t1)sumarlos\n\t2)restarlos (primero - segundo)\n\t3)multiplicar\n\t4)salir")

choice = int(input("¿Qué operación quiere realizar? "))

while choice != 4:
    if choice == 1:
        print(a+b)
        break
    elif choice == 2:
        print(a-b)
        break
    elif choice == 3:
        print(a*b)
        break
    elif choice == 4:
        break
    else:
        print("Opción inválida - las opciones son: 1, 2, 3 ó 4")
        choice = int(input("¿Qué operación quiere realizar? "))
    
