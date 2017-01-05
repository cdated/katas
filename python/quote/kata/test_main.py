import main
from mock import patch, call
from unittest import TestCase

class Test(TestCase):
    def test_read_input(self):
        with patch('main.input', return_value='valid input'):
            self.assertEqual(main.read_quotes(), 'valid input')

    def test_parse_quotes(self):
        expected = dict(me="yolo", you="polo")
        data = '("yolo" me) ("polo" you)'
        result = main.parse_quotes(data)
        self.assertEqual(expected, result)

    def test_parse_quotes_name(self):
        quote = "yolo"
        name = "Brandon T. Fields"
        expected = {name : quote}

        data = '("{}" {})'.format(quote, name)
        result = main.parse_quotes(data)

        self.assertEqual(expected, result)

    def test_parse_quote_long(self):
        quote = "What is the quote? These aren't the droids you're looking for."
        name = "Dr. Sherlock Holmes"
        expected = {name : quote}

        data = '("{}" {})'.format(quote, name)
        result = main.parse_quotes(data)

        self.assertEqual(expected, result)

    @patch('main.print')
    @patch('main.parse_quotes')
    @patch('main.read_quotes')
    def test_quote_output(self, read_quotes, parse_quotes, mock_print):
        read_quotes.return_value = ''
        parse_quotes.return_value = dict(me="yolo", you="polo")

        main.main()

        calls = [call('me says, "yolo"'), call('you says, "polo"')]
        self.assertEqual(mock_print.mock_calls, calls)
        self.assertTrue(read_quotes.call_count == 1)
        self.assertTrue(parse_quotes.call_count == 1)

    @patch('main.print')
    @patch('main.parse_quotes')
    @patch('main.read_quotes')
    def test_quote_empty(self, read_quotes, parse_quotes, mock_print):
        read_quotes.return_value = ''
        parse_quotes.return_value = dict()

        main.main()

        calls = [call('me says, "yolo"'), call('you says, "polo"')]
        self.assertNotEqual(mock_print.mock_calls, calls)
        self.assertTrue(read_quotes.call_count == 1)
        self.assertTrue(parse_quotes.call_count == 1)
