#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_dict = {'item':'football','price':10.00}
count=my_dict.get('count',0) # no error if key is not available
print(count)

count = my_dict.setdefault('count',0) # if count doesnt exist, create it and set it to 0
print(my_dict)
