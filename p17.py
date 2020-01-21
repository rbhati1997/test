"""
Question 23:
Write a method which can calculate square value of number.
"""
import math

#To get a string from console input.
input_value = input("Write a number: ")

def square_value(input_value):
	"""
	Funtion to print a square of given number.
	param:input_value
	"""
	print(input_value*input_value)

# Calling square value function.
square_value(input_value)
