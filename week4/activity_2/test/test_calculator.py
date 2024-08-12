import unittest
from src.Calculator import add
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(2.5, 2.5), 5)
        self.assertEqual(add(3 - 1j, 2 + 1j), (5 + 0j))

    def test_types(self):
        self.assertRaises(TypeError, add, "string", "string")
