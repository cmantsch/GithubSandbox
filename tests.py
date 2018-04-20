import unittest

class SomeTestCase(unittest.TestCase):
    def test_upper_case(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()