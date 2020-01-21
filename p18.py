"""
Question 24:
Python has many built-in functions, and if you do not know how to use it, you can read document
online or find some books. But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(),
raw_input()
And add document for your own function
"""

#To get a string from console input.
input_value = input("Write a built-in funtion name: ")

def document(input_value):
	"""
	Prints document of given function.
	param:input_string.
	"""

	if type(input_value) == tuple:

		for i in input_value:
			print(i.__doc__)

	print(input_value.__doc__)

# Calling document function.
document(input_value)
# Printing document of our own funtion.
print(document.__doc__)
