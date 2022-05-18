#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
variableDelitos = pd.read_csv('./delitos_2021.csv')
#print(variableDelitos.head(3))
# print(variableDelitos.tail())
# print(variableDelitos.sample(3)) # 3 al azar

#print(variableDelitos['id-mapa'].value_counts())
print(variableDelitos['subtipo'].value_counts().head())
