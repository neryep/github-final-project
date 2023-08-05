"""
Testing translator.py
"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"

        result = english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

        different_french_text = "Salut"
        self.assertNotEqual(result, different_french_text)

    def test_french_to_english(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"

        result = french_to_english(french_text)
        self.assertEqual(result, expected_english_text)

        different_english_text = "Hi"
        self.assertNotEqual(result, different_english_text)

if __name__ == '__main__':
    unittest.main()
