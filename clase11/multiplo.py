#!/usr/bin/env python
# -*- coding: utf-8 -*-

def multiplo(a,b):
    if a%b == 0:
        print(f'{b} es múltiplo de {a}')
        return 0
    else:
        print(f'{b} NO es múltiplo de {a}')
        return 1
multiplo(2,3)
multiplo(4,2)
