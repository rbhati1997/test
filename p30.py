"""
Question 38:
Define a function which can generate a list where the values are square of numbers between 1 and
20 (both included). Then the function needs to print the first 5 elements in the list.
"""
input_num = input("Write number:")
lis1=[]

def lis(n1,n2):
	"""
	Generate and print first 5 value of list.
	param:n1,n2
	"""
	i = 0
	if n1 and n2 <= 20:
		for x in range(n1,n2+1):
			lis1.append(x*x)

		for lis2 in lis1:
			if i <=4:
				print(lis2)
				i +=1
	else:
		print("Value out of range")

# Calling function.
lis(input_num[0],input_num[1])