"""
Question 27:
Define a function that can convert a integer into a string and print it in console.
"""

#To get a integer from console input.
input_value = int(input("Write a number: "))

def converter(integer):
	"""
	Convert integer into string.
	param:integer
	return:string of given numbers.
	"""
	print(str(integer))

# Call converter function.
converter(input_value)