class DiscountCalculator(object):
	def calculate(self, total, discount_amount, discount_type):
		percentage_discount = float(discount_amount) / 100
		discount = float(total) * percentage_discount
		return discount