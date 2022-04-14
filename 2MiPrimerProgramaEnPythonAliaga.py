#!/usr/bin/python3

nota_1 = int(input("Ingrese la nota del primer exámen: "))
nota_2 = int(input("Ingrese la nota del segundo exámen: "))

promedio_ponderado = (nota_1 * 0.4 + nota_2 * 0.6) / 1

print("Nota final promedio ponderado:", promedio_ponderado)
