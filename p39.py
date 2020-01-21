"""
Question 47:
Write a program which can map() and filter() to make a list whose elements are square of even
number in [1,2,3,4,5,6,7,8,9,10].
"""

def square(value):
	"""
	param:value
	return:square of param vlaue.
	"""
	return value*value

lis1 = [1,2,3,4,5,6,7,8,9,10]
# Fetching even number from given Lis1 using filter and Lambda function.
result1 = filter(lambda x: x%2==0, lis1)
# Fetching square of given even number list using map function.
result2 = map(square,result1)
print(result2)
