#!/usr/bin/python
# -*- coding: utf-8 -*-

#http://farmdev.com/src/secrets/magicmethod/#introducing-getitem

class Test(object):
    def __getitem__(self, items):
        print '%-15s  %s' % (type(items), items)

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]

'''
    <type 'int'>     1
    <type 'str'>     hello world
    <type 'tuple'>   (1, 'b', 3.0)
    <type 'slice'>   slice(5, 200, 10)
    <type 'slice'>   slice('a', 'z', 3)
    <type 'object'>  <object object at 0x00C10468>
'''