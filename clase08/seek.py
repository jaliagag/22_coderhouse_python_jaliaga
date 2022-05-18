#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('paraLeer.txt','r')

f.seek(20)
print(f.read())
f.close()
