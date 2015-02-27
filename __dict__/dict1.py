#!/usr/bin/python
# -*- coding: utf-8 -*-


'''- See more at: http://magmax.org/2013/09/30/python-avanzado.html#sthash.xsWbcEYG.dpuf

Atributos bajo demanda En python todo funciona como si fuera una tabla Hash o, en nomenclatura más pythónica, un diccionario. Existe un método mágico llamado __dict__, que es un atributo de sólo lectura que contine los valores del resto de atributos de un objeto. Y podemos aprovecharnos de esta propiedad para hacer objetos que "mutan" de acuerdo a su inicialización: - See more at:

http://magmax.org/2013/09/30/python-avanzado.html#sthash.xsWbcEYG.dpuf

'''

class Example(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

'''
>>> example = Example(var1=1, var2='hello')
>>> example.var
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Example' object has no attribute 'var'
>>> example.var1
1
>>> example.var2
'hello'
>>> 

'''