import re

passwords = raw_input("Enter password to test: ")

def validation(passwords):
	"""
	Function to check validation for given passwords.
	param: passwords.
	"""
	password_list = passwords.split(",")

	# iteration password_list.
	for password in password_list:

		if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])(?=.*[@#$])[A-Za-z\d@#$]{6,12}$', password):
			print(password)

# Calling validation function.
validation(passwords)