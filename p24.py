"""
Define a function that can accept an integer number as input and print the "It is an even number" if
the number is even, otherwise print "It is an odd number".
"""
input_num = input("Write a number: ")

def even_odd(n1):
	"""
	Funtion to check nuber is even or odd.
	param:s1,s2
	"""
	if n1 % 2 == 0:
		print("it is an even number.")
	else:
		print("it is an odd number.")

# Calling function.
even_odd(input_num)