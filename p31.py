"""
Question 39:
Define a function which can generate a list where the values are square of numbers between 1 and
20 (both included). Then the function needs to print the last 5 elements in the list.
"""

#To get a value from console input.
input_num = input("Write number:")
lis1=[]
lis2=[]

def lis(n1,n2):
	"""
	Generate and print last 5 element in list.
	param:n1,n2
	"""
	i = 0
	if n1 and n2 <= 20:
		for x in range(n1,n2+1):
			lis1.append(x*x)
		lis1.reverse()
		
		for y in lis1:
			if i <=4:
				lis2.append(y)
				i +=1
		print(lis2)
	else:
		print("Value out of range")

# Calling function.
lis(input_num[0],input_num[1])