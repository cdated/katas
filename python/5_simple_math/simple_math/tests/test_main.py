from simple_math import main
import mock
from unittest import TestCase


class Test(TestCase):

    def test_get_input(self):
        # Ensure numerical input
        with mock.patch('simple_math.main.input', return_value='1.0'):
            self.assertEqual(main.get_input(), 1.0)

        with mock.patch('simple_math.main.input', return_value='2'):
            self.assertEqual(main.get_input(), 2)

        with mock.patch('simple_math.main.input', return_value='-3'):
            self.assertEqual(main.get_input(), -3)

    def test_get_input_not_numeric(self):
        # Ensure only numerical input
        with mock.patch('simple_math.main.input', return_value='valid input'):
            with self.assertRaises(Exception):
                self.assertEqual(main.get_input(), 'valid input')

    @mock.patch('simple_math.main.print')
    @mock.patch('simple_math.main.get_input', return_value="Good day!")
    def test_main_print(self, mock_get_input, mock_print):
        greeting = "Good day!"
        main.main()

        calls = [mock.call(greeting)]
        self.assertEqual(mock_print.mock_calls, calls)
