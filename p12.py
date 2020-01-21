"""
Question 13: Write a program that accepts a sentence and calculate the number of letters and digits.
"""

#To get a string from console input.
sentence = raw_input("write a sentence=")

def calculate(sentence):
	"""
	Finction to calculate the number of letters and digits.
	param:sentence
	"""
	latters = 0
	numbers = 0
	
	# Loop for iterating a sentence.	
	for i in sentence:
		
		if i.isalpha():
			latters += 1
	
		if i.isdigit():
			numbers += 1
	
	print("Number={}".format(numbers))
	print("latters={}".format(latters))

# Calling function with argument.
calculate(sentence)
