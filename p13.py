"""
Question 14: Write a program that accepts a sentence and calculate the number of upper case letters
and lower case letters.
"""

#To get a string from console input.
sentence = raw_input("write a sentence=")

def calculate(sentence):
	"""
	Finction to calculate the number of upper case letters and lower case letters.
	param:sentence
	"""
	upper_case = 0
	lower_case = 0
	
	# Loop for iterating a sentence.	
	for i in sentence:
		
		if i.isupper():
			upper_case += 1
			
		if i.islower():
			lower_case += 1
	
	print("upper_case={}".format(upper_case))
	print("lower_case={}".format(lower_case))

# Calling function with argument.
calculate(sentence)
