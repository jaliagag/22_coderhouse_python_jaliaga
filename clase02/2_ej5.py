#!/usr/bin/env python
# -*- coding: utf-8 -*-

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

#for i in matriz:
#    a = matriz.index(i)
#    matriz[a].append(sum(matriz[a]))

print(matriz)
