import unittest
from city_functions import *

class NamesTestCase(unittest.TestCase):
    """testy dla programu city_function.py"""

    def test_city_country(self):

        long = long_information('santiago','chile')
        self.assertEqual(long,'Santiago , Chile ')
unittest.main()