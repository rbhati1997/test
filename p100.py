"""
Question 12: Write a program, which will find all such numbers between 1000 and 3000 (both
included) such that each digit of the number is an even number. The numbers obtained should be
printed in a comma-separated sequence on a single line.
"""

lis = []
for x in range(1000,3000):
	f=0
	x_string = str(x)

	for y in x_string:

		 if int(y)%2 !=0:
		 	f=1
		 	break

	if f==0:
	 	lis.append(int(x_string))
	
print(lis)