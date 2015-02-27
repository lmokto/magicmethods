#!/usr/bin/python
# -*- coding: utf-8 -*-

#http://stackoverflow.com/questions/1964934/what-is-contains-do-which-one-can-call-contains-function

class a(object):
    d='ddd'
    def __contains__(self, m):
        if self.d: return True
b=a()

'''
>>> 'd' in b
True
'''