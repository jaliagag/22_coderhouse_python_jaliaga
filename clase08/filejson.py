#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json 

data = {} # diccionario

data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17
})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Crazy',
    'age': 32,
    'amount': [9.27, 2.70]
})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 7.17
})

print(data)

with open('primerjson.json','w') as file:
    json.dump(data,file,indent=4)





