import unittest
from annual_salary import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.total_amount = Employee('sadaf','hina',30000)
       
    def test_give_raise_defualt(self):
        self.total_amount.give_raise()
        self.assertEqual(self.total_amount.salary,35000)

    def test_give_raise_custom(self):
        self.total_amount.give_raise(10000)
        self.assertEqual(self.total_amount.salary,40000)    


unittest.main()

