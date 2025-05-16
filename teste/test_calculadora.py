import sys
import os

# Adiciona o caminho src ao sys.path (antes das importações)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculadora import somar, subtrair
import unittest

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)
        self.assertEqual(subtrair(0, 3), -3)

if __name__ == '__main__':
    unittest.main()

#python -m unittest teste.test_calculadora