"""Question 3: With a given integral number n, write a program to generate a dictionary that contains
(i, i*i) such that is an integral number between 1 and n (both included). and then the program should
print the dictionary."""

# For command line input.
Number = int(input("Write a number:"))
d = {}
for x in range(1,Number+1):
	d.update({x:x*x})
print(d)

