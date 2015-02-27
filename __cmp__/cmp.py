#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
#http://magmax.org/2013/09/30/python-avanzado.html
'''

class StringContaining(object):
    def __init__(self, pattern):
        self._pattern = pattern
    def __cmp__(self, other):
        return self._pattern in other

called_me = StringContaining('MagMax')

if called_me('Hello, MagMax'):
    print('What do you want?')