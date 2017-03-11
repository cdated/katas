from kata import main
import mock
from unittest import TestCase


class Test(TestCase):

    def test_read_input(self):
        with mock.patch('kata.main.input', return_value='valid input'):
            self.assertEqual(main.get_input(), 'valid input')

    @mock.patch('kata.main.print')
    @mock.patch('kata.main.get_input', return_value="Good day!")
    def test_main_print(self, mock_get_input, mock_print):
        greeting = "Good day!"
        main.main()

        calls = [mock.call(greeting)]
        self.assertEqual(mock_print.mock_calls, calls)
