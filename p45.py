"""
Question 53:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle
class has a method which can compute the area.
"""
input_length = input("Write length here: ")
input_width = input("Write width here: ")

class Rectangle:
	"""
	Class to find area of rectangle.
	"""
	@staticmethod
	def area(l,b):
		"""
		param:l,b
		return:area of rectangle.
		"""
		return l*b

# Callin static method of Circle class.
area = Rectangle.area(input_length,input_width)
print(area)