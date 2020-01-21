"""
Question 15: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
value of a.
"""

num=input("Write a number here: ")
val='a+aa+aaa+aaaa'
sum=0

# Replace 'a' with given number.
val1=val.replace('a',str(num))
# Split val1.
val2=val1.split('+')

for x in val2:
	sum+=int(x)

print(sum)
