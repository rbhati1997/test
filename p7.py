import math
"""
Question 6: Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
"""

# For taking input from console/user.
seq = input("Write sequence of numbers:")
lis = []

def formula(D):
	"""
	param:D
	return:square root of given values.
	"""
	C, H = 50, 30
	return int(math.sqrt((2*C*D)/H))

# Loop to iterate user given input.
for x in seq:
	lis.append(formula(x))

# For removing square brackets from list.
print( ", ".join( repr(e) for e in lis ) )