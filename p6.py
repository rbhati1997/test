"""
Question 4: Write a program which accepts a sequence of comma-separated numbers from console
and generate a list and a tuple which contains every number.
"""

# For taking input from console/user.
seq = input("Write sequence of numbers:")
lis = []
for x in seq:
	lis.append(str(x))

print(lis)
print(tuple(lis))
