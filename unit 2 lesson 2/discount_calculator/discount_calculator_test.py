import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
	def test_ten_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100,10,'percent')
		self.assertEqual(10.0, result)	

	def fifteen_percent_discount_test(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100,15,'percent')
		self.assertEqual(15.0, result)

	def invalid_discount_type_test(self): 
		discount_calculator = DiscountCaclualtor() 
		self.assertRaises(ValueError, discount_calculator.calculate, 250, 5, 'random')

	def floating_point_percentage_discount_test(self):
		# confirms that the percentage code works with floating point inputs
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100.0,10.0,'percent')
		self.assertEqual(10.0, result)

	def floating_point_absolute_discount_test(self):
		# tests the absolute discount code 
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(250.0,5.0,'absolute')
		self.assertEqual(5.0, result)

	def excessive_discount_type_test(self):
		#tests if the discount is excessive =] 
		discount_calculator = DiscountCalculator()
		self.assertRaises(ValueError, discount_calculator.calculate, 
		250, 110, 'percent')

	def excessive_absolute_discount_test(self):
		#tests if the absolute dsicount is more than the total price
	    discount_calculator = DiscountCalculator()
	    self.assertRaises(ValueError, discount_calculator.calculate, 250, 260, 'absolute')







	


