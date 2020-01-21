"""
Question 48:
Write a program which can filter() to make a list whose elements are even number between 1 and
20 (both included).
"""
input_value = input("Write integer values: ")
lis1 = []

for x in input_value:
	if x <= 20:
		lis1.append(x)

resut = filter(lambda x: x%2==0,lis1)
print(resut)