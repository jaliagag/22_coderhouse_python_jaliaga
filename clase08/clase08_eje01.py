#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('petfile.txt','w')

pet = {'Name':'','Animal':'','Race':'','Age':''}

for i in pet.keys():
    a = input(f"What's your pet's {i}: ")
    pet[i] = a

f.write(pet['Name'] +',' + pet['Animal'] + ',' + pet['Race'] + ',' + pet['Age'] + '\n')
f.close()
print()
r = open('petfile.txt','r')
print(r.read())
r.close()
