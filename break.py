#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = 5
while n < 10:
    n -= 1
    if n == 2:
        print("ahora que n vale 2 salimos")
        break
    print("n vale", n)

c = -3
while True:
    c += 1
    if c == 2:
        print("ahora que c vale 2 salimos")
        break
    print("c vale", c)
