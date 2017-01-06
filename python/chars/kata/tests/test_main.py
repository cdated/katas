from kata import main
from mock import patch
from unittest import TestCase

class Test(TestCase):
    def test_homer(self):
        with patch('kata.main.input', return_value='Homer'):
            self.assertEqual(main.num_chars(), 'Homer has 5 characters.')

    def test_brandon(self):
        with patch('kata.main.input', return_value='Brandon'):
            self.assertEqual(main.num_chars(), 'Brandon has 7 characters.')

    def test_empty(self):
        with patch('kata.main.input', return_value=''):
            self.assertEqual(main.num_chars(), 'A string must be provided.')

    def test_not_homer(self):
        with patch('kata.main.input', return_value='Marge'):
            self.assertNotEqual(main.num_chars(), 'Homer has 5 characters.')
