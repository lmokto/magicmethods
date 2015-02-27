#!/usr/bin/python
# -*- coding: utf-8 -*-

#http://farmdev.com/src/secrets/magicmethod/#introducing-getitem

class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
    def __setattr__(self, name, value):
        print 'set %s clink %s' % (name, repr(value))
        if name in ('a', 'b'):
            object.__setattr__(self, name, value)

