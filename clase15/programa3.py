#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) == 3:
    text = sys.argv[1] # accedemos a los argumentos
    repeticiones = int(sys.argv[2])

    for r in range(repeticiones):
        print(text)
else:
    print("error: introduce los argumentos correctamente")
    print('ejemplo: programa3.py texto 5')
