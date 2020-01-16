"""
Question:5
two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""

class Example:
	"""
	This to perform action of get_string and print_string function.
	"""
	def print_string(self,input_string):
		print(input_string.upper())

	def get_string(self):
		#To get a string from console input.
		input_string = raw_input("Write a string: ")
		return self.print_string(input_string)

# Make object of class.
obj = Example()
# Call get_string function.
obj.get_string()