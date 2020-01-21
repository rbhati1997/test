"""
Question 17: Write a program that computes the net amount of a bank account based a transaction
log from console input
"""

#To get deposite amount from console input.
D = raw_input("How much want to deposite=")
#To get withdraw amount from console input.
W = raw_input("How much want to withdraw=")

def calculate(D=None,W=None):
	"""
	Funtion to computes the net amount of a bank account based a transaction.
	param:D,W
	"""
	amount = 0

	if D:
		amount += int(D)
	if D > W:
		amount -= int(W)
	else:
		print("Don't have sufficient balance to withdraw.")
	print("total amount={}".format(amount))

# Calling calculate function with argument.
calculate(D,W)