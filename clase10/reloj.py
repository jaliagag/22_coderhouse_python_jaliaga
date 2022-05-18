#!/usr/bin/env python
# -*- coding: utf-8 -*-

def watch(**kwargs):
    seconds = 0
    minutes = 0
    hours = 0
    if len(kwargs) == 1:
        for key,value in kwargs.items():
            minutes = int(value/60) # minutos
            if minutes >= 60:
                hours = int(minutes / 60)
                minutes -= (hours*60)
            seconds = value - (hours*60*60) - (minutes*60)
        print(f'{hours}:{minutes}:{seconds}')
    elif len(kwargs) == 3:
        for key,value in kwargs.items():
            if key == 'a':
                seconds += value*60*60
            elif key == 'b':
                seconds += value*60
            elif key == 'c':
                seconds += value 
        print(seconds)
    else:
        print('no tiene ni uno ni 3 argumentos')

    return hours,minutes,seconds

watch(a=6903)
watch(a=1,b=55,c=3)
