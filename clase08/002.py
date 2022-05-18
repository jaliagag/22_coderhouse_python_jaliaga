#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = 'jose'
last = 'aliaga'
idn = 111111

d = {'name':name,'lastname':last,'id':idn}

f = open('otro.txt','w')

f.write(d['name']+','+d['lastname']+','+str(d['id']))

f.close()
