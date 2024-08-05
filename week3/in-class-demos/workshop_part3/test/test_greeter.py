import unittest


from greeter import greet
class TestGreeter(unittest.TestCase):
    def test_greet(self):
        assert greet("John") == ("Hello John")
        self.assertEqual(greet("John"), "Hello John")


