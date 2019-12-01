# -*- coding: utf-8 -*-

import unittest

from spellcheckerCA import SpellChecker

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')


    def test_dictionary_of_words(self):
        self.assertTrue(len(self.spellChecker.words) == 53751)


    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_document('spell.words'))
        self.assertTrue(self.spellChecker.check_document('text1.words'))
        self.assertFalse(self.spellChecker.check_word('mistasdas'))
        self.assertTrue(
            len(self.spellChecker.check_words('zygotic mistasdas elementary')) == 1)
        self.assertTrue(len(self.spellChecker.check_words('our first correct sentence')) == 0)
        self.assertTrue(len(self.spellChecker.check_words('Our first correct sentence.')) == 0)
        self.assertEqual(2,
            len(self.spellChecker.check_document('spell.words')))
        failed_words = self.spellChecker.check_words('wrooongggg wooord to be detected')
        self.assertTrue(len(failed_words) == 2)
          

    def test_check_profanities(self):
        self.assertTrue(self.spellChecker.check_profanities('sht'))                   
        failed_profane_words = self.spellChecker.check_document('profanity.txt')
        self.assertEqual(921, len(failed_profane_words))
        self.assertEqual('profanity', failed_profane_words[0]['type'])    
        
        
    def test_check_folder(self):
        self.assertFalse(self.spellChecker.check_folder('*.words'))
        
if __name__ == '__main__':
    unittest.main()
