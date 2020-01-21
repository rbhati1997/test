"""
Question 42:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
and the last half values in one line.
"""
tup1 = (1,2,3,4,5,6,7,8,9,10)
tup_lis1 = []
tup_lis2 = []
i=0
for x in tup1:
	if i <= (len(tup1)/2)-1:
		tup_lis1.append(x)
		i+=1
	else:
		tup_lis2.append(x)
print(tuple(tup_lis1))
print(tuple(tup_lis2))
