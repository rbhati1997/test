"""
Question 2: Write a program which can compute the factorial of a given numbers. The results
should be printed in a comma-separated sequence on a single line.
"""
input_number = input("Write a number: ")
i = 1

for x in range(1,input_number+1):
	i = i*x

print(i)

