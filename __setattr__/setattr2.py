#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Diccionarios que se comportan como objetos Otra característica que puede sernos de utilidad es tener un diccionario que se comporta como un objeto, es decir, que permite acceder a sus elementos como atributos. Esta característica puede hacer nuestro código más fácil de leer: - See more at: http://magmax.org/2013/09/30/python-avanzado.html#sthash.xsWbcEYG.dpuf'''

class DictObject(dict):
    def __getattr__(self, name):
        return self[name]
    def __setattr__(self, name, value):
        self[name] = value


'''
>>> example1 = DictObject()
>>> example1['one'] = 'hello'
>>> example1.one
'hello'
>>> example1['one']
'hello' 

#WRONG

>>> example = DictObject()
>>> example[1] = 'hello'
>>> example[1] 'hello'
>>> example.1 SyntaxError: invalid syntax >>>
'''