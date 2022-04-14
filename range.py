#!/usr/bin/env python
# -*- coding: utf-8 -*-

for numero in range (10):
    print("numero vale", numero)
else:
    print("se terminó de iterar! numero vale:",numero)

for n in range(10):
    if n == 2:
        continue
    elif n == 8:
        break
    print("n vale", n)
else:
    print("se terminó de iterar y n vale", n)

