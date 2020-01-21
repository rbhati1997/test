"""
Question 43:
Write a program to generate and print another tuple whose values are even numbers in the given
tuple (1,2,3,4,5,6,7,8,9,10).
"""
tup1 = (1,2,3,4,5,6,7,8,9,10)
tup_lis1 = []

for x in tup1:
	if x%2==0:
		tup_lis1.append(x)

# Convert list into tuple and print.
print(tuple(tup_lis1))

