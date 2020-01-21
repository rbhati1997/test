"""
Question 30:
Define a function that can accept two strings as input and concatenate them and then print it in
console.
"""

input_string1 = raw_input("Write a string1: ")
input_string2 = raw_input("Write a string2: ")

def concatenate(s1,s2):
	"""
	Function for concatenate two strings.
	param: s1,s2.
	"""
	print(s1 + " " + s2)

# Caliing function.
concatenate(input_string1,input_string2)