#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = [3,5,1,10,9]

sorted_data = sorted(data)

print(sorted_data)

data = [{'name':'jose','age':32},
        {'name':'pau','age':33},
        {'name':'alfon','age':2}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)
