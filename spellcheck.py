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

def check_words(words, sentence):
    words_to_check = sentence.split(' ')
    for word in words_to_check:
        if not check_word(words, word):
            print('Word is misspelt : ' + word)
            return False
    return True

words = load_words('spell.words')
print(check_word(words, 'zygotic'))
print(check_words(words, 'zygotic mistasdas elementary'))
