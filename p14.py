"""
Question 16: Use a list comprehension to square each odd number in a list. The list is input by a
sequence of comma-separated numbers.
"""

#To get a number from console input.
numbers = input("Write numbers=")
lis = []

def odd_num(numbers):
	"""
	Function to find and append odd number in a list.
	param:numbers
	"""
	for i in numbers:
		if i % 2 != 0:
			lis.append(i)

# Calling even_num function.
odd_num(numbers)
print(str(lis)[1:-1])
