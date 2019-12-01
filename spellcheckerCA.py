# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:24:18 2019

@author: raphl
"""

# -*- coding: utf-8 -*-


import glob


class SpellChecker(object):
    def __init__(self):
        self.words = []

    def load_file(self, file_name):
        lines = open(file_name).readlines()
        return list(map(lambda x: x.strip().lower(), lines))

    def load_words(self, file_name):
        self.words = self.load_file(file_name)

    def check_profanities(self, word):
        return word not in ['fuck', 'shit']
        
    def check_word(self, word):
        return word.lower().strip('().,-:?\"') in self.words
    
    def check_words(self, sentence, index=0):
        failed_words = []
        words_to_check = sentence.split(' ')
        caret_position = 0
        for word in words_to_check:
            if not self.check_word(word):
                failed_words.append(
                    {'word':word, 'line':index+1,
                        'pos':caret_position+1, 'type': 'spelling'})
            if not self.check_profanities(word):
                failed_words.append(
                    {'word':word, 'line':index+1,
                        'pos':caret_position+1, 'type': 'profanity'})
            caret_position += len(word) + 1
        return failed_words

    def check_document(self, file_name):
        failed_words_in_sentences = []
        self.sentences = self.load_file(file_name)
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(
                self.check_words(sentence, index))
        return failed_words_in_sentences
    
    def check_folder(self,word_files):
        word_files_in_folder=[]
        files_in_folder_to_check=glob.glob(word_files)       
        for file in files_in_folder_to_check:
            print(spell_checker.check_document(file))
            word_files_in_folder.append(1)
        print('Number of checked files --> {}'.format(len(word_files_in_folder)))
        
        
if __name__ == '__main__':
  
    spell_checker = SpellChecker()
    spell_checker.load_words('spell.words')
    spell_checker.check_folder('*.words')



    
    