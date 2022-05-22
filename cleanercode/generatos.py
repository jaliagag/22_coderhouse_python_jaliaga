#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

my_list=[i for i in range(1000)]
print(sum(my_list))
print(sys.getsizeof(my_list),"bytes")

# este es el generador
my_gen=(i for i in range(1000))
print(sum(my_gen))
print(sys.getsizeof(my_gen),"bytes")
