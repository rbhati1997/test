"""
Question 31:
Define a function that can accept two strings as input and print the string with maximum length in
console. If two strings have the same length, then the function should print al l strings line by line.
"""

input_string1 = raw_input("Write a string1: ")
input_string2 = raw_input("Write a string2: ")

def max(s1,s2):
	"""
	Funtion to print the string with maximum length.
	param:s1,s2
	"""
	if len(s1) > len(s2):
		print(s1)
	elif len(s1) < len(s2):
		print(s2)
	else:
		print(s1 + "\n" + s2)

# Calling function.
max(input_string1,input_string2)