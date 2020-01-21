"""
Question 52:
Define a class named Circle which can be constructed by a radius. The Circle class has a method
which can compute the area.
"""
input_radius = input("Write radius hare: ")

class Circle:
	"""
	Class to find area of circle.
	"""
	@staticmethod
	def area(r):
		"""
		Calculate area of circle.
		param:r
		return:area of circle.
		"""
		pi = 3.14
		return pi*(r*r)

# Callin static method of Circle class.
area = Circle.area(input_radius)
print(area)