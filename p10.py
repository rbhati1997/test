"""
Question 11: Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not. The numbers that are
divisible by 5 are to be printed in a comma separated sequence.
"""

#To get a string from console input.
binary_num = input("Write 4 digit binary number:")

def binary(binary_num):
	"""
	Funtion to print number which are divisible by 5.
	"""
	for n in binary_num:
		if n % 5 == 0:
			print(n)

# Calling binary function with argument.
binary(binary_num)