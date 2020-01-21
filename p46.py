"""
Question 54: Define a class named Shape and its subclass Square. The Square class has an init
function which takes a length as argument. Both classes have a area function which can print the
area of the shape where Shape's area is 0 by default.
"""
# shape = 0

class Shape:
		
	def area(self):
		return 0

class Square:
	"""
	Print the area of the shape.
	"""
	def __init__(self,length):
		self.length = length

	def area(self):
		print(self.length*self.length)

input_length=input("Write a length here: ")
obj = Square(input_length)
obj.area()