"""
Question 10: Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
"""
# Taking input from console.
input_string = raw_input("Write sequrnce of word: ")
# Spliting a given string.
string1 = input_string.split(" ")
# Removing duplicate elements.
string2 = list(dict.fromkeys(string1))
# Sorting elements.
string2.sort()
print(" ".join(string2))