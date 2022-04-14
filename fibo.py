#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 0
b = 1

c = 0

while b < 100000000:
    c = a + b
    a = b
    b = c
    print(b)


