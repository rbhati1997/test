"""
Question 7: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be i*j.
"""

input_num=input("Enter Digits: ")

num1=input_num[0]
num2=input_num[1]
lis1=[]


def dimension(num1,num2):
	"""
	Generates a 2-dimensional array.
	"""
	for x in range(num1):
	    lis2=[]
	    for y in range(num2):
	        lis2.append(x*y)
	    lis1.append(lis2)

# Calling funtion.
dimension(num1,num2)
print(lis1)