"""
Question:5
two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""

#To get a string from console input.
input_string = str(input("Write a string:"))


def get_string(input_string):
	"""
	:param input_string:
	:return:calling a print_string function.
	"""
	print(input_string)
	return print_string(input_string)

def print_string(input_string):
	"""
	:param input_string:
	:return: Upper-case of given string.
	"""
	upper_case = input_string.upper()
	print(upper_case)
	return upper_case

# Calling get_string function with argument.
get_string(input_string)

