"""
Question 61: Please write a program which accepts a string from console and print the characters
that have even indexes.
"""

input_string = raw_input("Write string here: ")
lis1 = []

for x in input_string:
	if input_string.index(x)%2==0:
		lis1.append(x)

print("".join(lis1))