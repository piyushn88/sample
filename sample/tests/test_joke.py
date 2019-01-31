from unittest import TestCase

from pip._vendor.pyparsing import basestring

import sample


class TestJoke(TestCase):
    def test_is_string(self):
        s = sample.joke()
        self.assertTrue(isinstance(s, basestring))