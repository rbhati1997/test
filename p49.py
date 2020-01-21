"""
Question 57:
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list
whose elements are intersection of the above given lists.
"""
lis1 = [1,3,6,78,35,55]
lis2 = [12,24,35,24,88,120,155]
lis3 = []

def intersec(l1,l2):
	"""
	Print a list whose elements are intersection.
	"""
	for value1 in lis2:
		if value1 in lis1:
			lis3.append(value1)
	print(lis3)

# Calling funtion.
intersec(lis1,lis2)