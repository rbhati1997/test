"""
Question 58:
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after
removing all duplicate values with original order reserved.
"""
lis1 = [12,24,35,24,88,120,155,88,120,155]
lis3 = []
def intersec(l1):
	"""
	Removing all duplicate values with original order reserved.
	"""
	# Removing duplicate elements from list.
	lis2 = list(dict.fromkeys(l1))
	
	for x in range(len(lis2)):
		# Reverse the order of list.
		lis3.append(lis2.pop())

# Calling function.
intersec(lis1)
print(lis3)