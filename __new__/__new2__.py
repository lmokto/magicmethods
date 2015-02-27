#!/usr/bin/python
# -*- coding: utf-8 -*-

import types
 
'''
http://crysol.org/es/metaprogramacion-con-python

Ya toca escribir una metaclase que haga algo útil por poco que sea. Esta metaclase crea automáticamente métodos que se llaman “not_[método]’ para cada método de la clase. Estos métodos devuelven el valor lógico negado de la función original.
'''

class AutoNot(type):
    def __init__(cls, name, bases, dct):
       type.__init__(cls, name, bases, dct)
       methods = [x for x in dct if isinstance(dct[x], types.FunctionType)] 
       for m in methods:
           setattr(cls, 'not_%s' % m, lambda self: not dct[m](self))
 
A = AutoNot('A', (), {'yes': lambda self:True})
a = A()
 
print a.yes()
print a.not_yes()