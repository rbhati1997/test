"""
Question 45:
Write a program which can filter even numbers in a list by using filter function. The list is:
[1,2,3,4,5,6,7,8,9,10].
"""
Lis1 = [1,2,3,4,5,6,7,8,9,10]

# Fetching even number from given Lis1 using filter and Lambda function.
result = filter(lambda x: x%2==0, Lis1)

print(result)