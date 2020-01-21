
"""
Question 49:
Write a program which can map() to make a list whose elements are square of numbers between 1
and 20 (both included).
"""
input_value = input("Write integer values: ")
lis1 = []

for x in input_value:
	if x <= 20:
		lis1.append(x)

# Fetching square of given list using map function.
resut = map(lambda x: x*x,lis1)
print(resut)