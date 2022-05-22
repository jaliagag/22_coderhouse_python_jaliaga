#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = [1,2,-3,-5]

# instead of for i in range(len(data))
for i,num in enumerate(data):
    if num < 0:
        data[i]=0

print(data)
