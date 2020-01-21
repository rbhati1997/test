"""
Question 29:
Define a function that can receive two integral numbers in string form and compute their sum and
then print it in console
"""

#To get a number from console input.
input_value = raw_input("Write a number: ")
input_list = input_value.split(",")

def sum(num1,num2):
	"""
	Receive two integral numbers in string form and compute their sum.
	param:num1, num2
	return:Sum of given numbers.
	"""
	return int(num1) + int(num2)

#Printing and calling sum function.
print(sum(input_list[0],input_list[1]))
