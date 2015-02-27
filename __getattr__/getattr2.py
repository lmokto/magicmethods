#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
http://magmax.org/2013/09/30/python-avanzado.html

Existen algunos métodos que nos permiten alterar el comportamiento habitual de nuestras clases. Por ejemplo, está el método __getattr__, que se ejecutará cuando tratemos de acceder a un atributo que no exista y, por lo tanto, podremos alterar el comportamiento habitual que consiste en lanzar una excepción:

- See more at: http://magmax.org/2013/09/30/python-avanzado.html#sthash.xsWbcEYG.dpuf

'''


class Example1(object):
    pass

class Example2(object):
    def __getattr__(self, attr):
        print 'invalid attribute:', attr


e1 = Example1()
e1.whatever

e2 = Example2()
e2.whatever

'''
Traceback (most recent call last):
  File "/home/delkar/Desktop/__getattr__/getattr2.py", line 10, in <module>
    e1.whatever
AttributeError: 'Example1' object has no attribute 'whatever'

'''