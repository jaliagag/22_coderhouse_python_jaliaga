#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vector:
  def __init__(self,data):
    self.data = data
  def __str__(self):
      return f"{self.data}"
  def __len__(self):
    return len(self.data)
  def __getitem__(self,pos):
    return self.data[pos]
  def __setitem__(self,pos,value):
    self.data[pos] = value

v = Vector([1,2])
print(v)
v[1]=20 # acá estamos usando el setitem
print(v)
