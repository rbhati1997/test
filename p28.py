"""
Question 36:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20
(both included) and the values are square of keys. The function should just print the keys only.
"""
input_num = input("Write number:")
dict1=dict()

def dic(n1,n2):
	"""
	function to generate and print keys of a dictionary.
	param:n1,n2
	"""
	if n1 and n2 <= 20:
		for x in range(n1,n2+1):
			dict1.update({x:x*x})

		for values in dict1.keys():
			print(values)
	else:
		print("Value out of range")

# Calling function.
dic(input_num[0],input_num[1])
