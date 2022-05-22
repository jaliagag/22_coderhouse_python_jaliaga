#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = 0
while n < 10:
    n += 1
    if n==2:
        #print("continuemos!")
        #break
        # si pongo pass, se imprime "continuemos" y "n vale 2"
        # si pongo continue, se imprime solamente "continuemos" - rompe LA ITERACIÓN pero no el bucle
        #continue
        pass 
    print("n vale", n)
