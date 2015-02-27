#!/usr/bin/python
# -*- coding: utf-8 -*-
import types
#http://crysol.org/es/metaprogramacion-con-python

 
class AutoNot(type):
    def __init__(cls, name, bases, dct):
       type.__init__(cls, name, bases, dct)
       methods = [x for x in dct if isinstance(dct[x], types.FunctionType)] 
       for m in methods:
           setattr(cls, 'not_%s' % m, lambda self: not dct[m](self))

class MyMetaclase3(type):
    def __new__(meta, name, bases, dct):
        print 'Creando la clase', meta
        return type.__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print 'Inicializando la clase', cls
        type.__init__(cls, name, bases, dct)



X = MyMetaclase3('X', (), {})
x1 = X()


A = AutoNot('A', (), {'yes': lambda self:True})
a = A()
 
print a.yes()
print a.not_yes()