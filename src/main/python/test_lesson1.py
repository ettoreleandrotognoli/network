from unittest import TestCase

from lesson1 import *

class TestLayer(TestCase):

    def test_soma(self):
        self.assertEquals(soma(2,2),4)
