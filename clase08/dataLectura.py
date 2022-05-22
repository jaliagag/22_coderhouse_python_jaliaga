#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json 

#f = open('primerJson.json','w')
#f.close()

with open('primerJson.json') as file:

    dataLectura = json.load(file)

    for client in dataLectura['clients']:
        print('First name:',client['first_name'])
        print('Last name:',client['last_name'])
        print('Age:',client['age'])
        print('Amount:',client['amount'])
        print('')
