import main
from mock import patch, call
from unittest import TestCase

class Test(TestCase):
    def test_read_input(self):
        with patch('main.input', return_value='valid input'):
            self.assertNotEqual(main.main(), 'valid input')
