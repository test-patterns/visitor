""" Sample problem featuring the visitor pattern. """

import unittest

from test_context import Cheese

class TestCheese(unittest.TestCase):
    """ Tests the Cheese class """

    def test_init(self):
        """ Tests the constructor of the Cheese class """
        test_cheese = Cheese(1.23)
        self.assertEqual(test_cheese.get_price(), 1.23)

if __name__ == '__main__':
    unittest.main()
