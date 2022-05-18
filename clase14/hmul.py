#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Clase1:
  pass
class Clase2(Clase1):
  pass
class Clase3(Clase2):
  pass

print(Clase3.__mro__)
