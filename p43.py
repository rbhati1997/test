"""
Question 51:
Define a class named American and its subclass NewYorker.
"""
input_nationality = raw_input("Write your nationality: ")

class American:
	"""
	Parent class of NewYork and have a static method.
	"""
	@staticmethod
	def nationality(input_nationality):
		print("My nationality is " + input_nationality)


class NewYork(American):
	"""
	Sub-class of American class
	"""		
	pass

# Object of class NewYork.
b_class = NewYork()
# Calling parent class method by sub-class object.
b_class.nationality(input_nationality)