"""
Question 26:
Define a function which can compute the sum of two numbers.
"""

#To get a number from console input.
input_value = input("Write a number: ")

def sum(num1,num2):
	"""
	param:num1, num2
	return:Sum of given numbers.
	"""
	return num1 + num2

# Check type of input_value.
if type(input_value) == tuple:
	#Printing and calling sum function.
	print(sum(input_value[0],input_value[1]))
else:
	print("Please provide valid value.")