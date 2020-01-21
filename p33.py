"""
Question 41:
Define a function which can generate and print a tuple where the value are square of numbers
between 1 and 20 (both included).
"""
input_num = input("Write number:")
lis1=[]

def lis(n1,n2):
	"""
	Generate and print tuple where the values are square of numbers.
	param:n1,n2
	"""
	if n1 and n2 <= 20:
		for x in range(n1,n2+1):
			lis1.append(x*x)
		print(tuple(lis1))
		
	else:
		print("Value out of range")

# Calling function.
lis(input_num[0],input_num[1])
