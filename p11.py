"""
Question 12: Write a program, which will find all such numbers between 1000 and 3000 (both
included) such that each digit of the number is an even number. The numbers obtained should be
printed in a comma-separated sequence on a single line.
"""

#To get a number from console input.
first_num = int(input("Write first number="))
second_num = int(input("Write second number="))
lis = []

def even_num(first_num,second_num):
	"""
	Function to append even number in a list.
	param:first_num, second_num
	"""
	for i in range(first_num,second_num):
		if i % 2 == 0:
			lis.append(i)

# Calling even_num function.
even_num(first_num,second_num)
print(str(lis)[1:-1])
