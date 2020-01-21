"""
Question 44:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or
"Yes", otherwise print "No".
"""
input_string = raw_input("Write a string here: ")

if input_string in ['yes','YES','Yes']:
	print("Yes")

else:
	print("No")