import unittest
from translator import english_to_french, french_to_english

class TestEnglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test eng
    def test2(self): 
        self.assertRaises(ValueError, english_to_french, None)

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test fr
    def test2(self): 
        self.assertRaises(ValueError, french_to_english, None)
unittest.main()
