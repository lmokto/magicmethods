#!/usr/bin/python
# -*- coding: utf-8 -*-

#http://farmdev.com/src/secrets/magicmethod/#introducing-getitem
#Implementing __getattr__ overrides Python's default mechanism for member access.


class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
    def __getattr__(self, name):
        return False


t = Test()
print 'object variables: %r' % t.__dict__.keys()
print t.a
print t.b
print t.c
print getattr(t, 'd')
print hasattr(t, 'x')