"""
Question 33:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both
included) and the values are square of keys.
"""
input_num = input("Write number:")
dict1=dict()

def dic(n1,n2):
	"""
	function to print a dictionary.
	param:n1,n2
	"""
	if n1 and n2 <= 3:
		for x in range(n1,n2+1):
			dict1.update({x:x*x})
	else:
		print("Value out of range")

# Calling function.
dic(input_num[0],input_num[1])
print(dict1)