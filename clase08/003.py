#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('paraLeer.txt','r')
#content = f.read()
#print(f.read()) # el archivo entero
#print(f.readline()) # solo la primera línea 
for i in f.readlines():
    print(i)

f.close()
