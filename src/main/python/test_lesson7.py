from unittest import TestCase
from lesson7 import *

class TestCesar(TestCase):
    def test_encode_decode(self):
        cesar = CesarCypher()
        origin = 'ettore'
        data = cesar.encode(origin)
        decoded = cesar.decode(data)
        self.assertEqual(origin,decoded)