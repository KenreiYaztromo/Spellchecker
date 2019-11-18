# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 00:42:50 2019

@author: raphl
"""

words = open('spell.words').readlines()
words = list(map(lambda x: x.strip(), words))
print('zygotic' in words)

def load_words(file_name):
    words = open(file_name).readlines()
    return list(map(lambda x: x.strip(), words))

def check_word(words, word):
    return word in words

words = load_words('spell.words')
# now check if the word zygotic is a word
print(check_word(words, 'zygotic'))

