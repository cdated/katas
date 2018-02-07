from kata import hello
from mock import patch
from unittest import TestCase

class Test(TestCase):
    def test_hello_brandon(self):
        with patch('kata.hello.input', return_value='Brandon'):
            self.assertEqual(hello.greeting(), 'Hello, Brandon, nice to meet you!')

    def test_hello_brian(self):
        with patch('kata.hello.input', return_value='Brian'):
            self.assertEqual(hello.greeting(), 'Sup Brian!')

    def test_hello_bob(self):
        with patch('kata.hello.input', return_value='Bob'):
            self.assertEqual(hello.greeting(), 'Hello, Bob, I hope you are well.')

    def test_hello_not_brandon(self):
        with patch('kata.hello.input', return_value='Brian'):
            self.assertNotEqual(hello.greeting(), 'Hello, Brandon, nice to meet you!')
