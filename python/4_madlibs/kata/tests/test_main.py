from kata import main
from unittest import TestCase
import mock


class Test(TestCase):

    def test_template(self):
        tpl = main.TEMPLATE
        self.assertTrue(isinstance(tpl, str))

    def test_get_answers(self):
        expected = dict(noun='a', verb='b', adjective='c', adverb='d')
        answers = ['a', 'b', 'c', 'd']

        main.input = mock.Mock(side_effect=answers)
        values = main.get_answers()
        self.assertEqual(values, expected)

    @mock.patch('kata.main.print')
    def test_main(self, mock_print):
        main.TEMPLATE = template = "{vala} + {valb}"
        values = dict(vala='a', valb='b')

        expected = template.format(**values)
        main.get_answers = mock.Mock(return_value=values)
        main.main()
        self.assertEqual(mock_print.mock_calls, [mock.call(expected)])
