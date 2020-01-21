"""
Question 50:
Define a class named American which has a static method called printNationality.
"""
input_nationality = raw_input("Write your nationality: ")

class American:
	"""
	Class have static method.
	"""
	@staticmethod
	def nationality(input_nationality):
		"""
		To print nationality.
		param:input_nationality
		"""
		print("My nationality is " + input_nationality)

# Calling nationality method.
American.nationality(input_nationality)