"""
Question 60:
Please write a program which accepts a string from console and print it in reverse order.
"""

input_string = raw_input("Write a string here: ")

def reverse_order(s):
	"""
	Print string in reverse order.
	param:s
	"""
	print(",".join((list(reversed(s)))))

# Calling function.
reverse_order(input_string)
