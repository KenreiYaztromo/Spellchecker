# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 00:42:50 2019

@author: raphl
"""

words = open('spell.words').readlines()
words = list(map(lambda x: x.strip(), words))
print('zygotic' in words)

