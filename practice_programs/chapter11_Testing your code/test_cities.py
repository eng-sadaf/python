import unittest
from city_functions import names
class FullNameTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""
    def test_city_country(self):
        """Do names like 'Santiago , Chile' work?"""
        formatted_name = names('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago , Chile')
 
    def test_city_country_population(self):
        """Do names like 'Santiago , Chile' work?"""
        formatted_name = names('santiago' , 'chile' , 5000000)
        self.assertEqual(formatted_name, 'Santiago , Chile , Population = 5000000')

if __name__ == '__main__':
    unittest.main()