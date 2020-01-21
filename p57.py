"""
Question 20:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a
given range 0 and n.
"""
input_num = input("Write a number: ")

class Gen:

	@staticmethod
	def gen_func(num):
		"""
		A simple generator function.
		"""
		for x in range(num):
			if x%7==0:
				yield x
				
# Using for loop to iterate numbers.
for num1 in Gen.func(input_num):
	print(num1)

