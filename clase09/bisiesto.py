#!/usr/bin/env python
# -*- coding: utf-8 -*-

def leap_year(year):
    if type(year) == int:
        if year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            a = print(f'El año {year} es bisiesto')
            return a
        else:
            a = print(f'El año {year} no es bisiesto')
            return a
    else:
        print(f'{year} no es un número')
    
years = [2010,2012,1992,2000,1900,"2022"]
for i in years:
    leap_year(i)

#while True:
#    ques = int(input('¿Qué año? '))
#    if ques == 0:
#        break
#    else:
#        leap_year(ques)



