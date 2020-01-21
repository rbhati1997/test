"""
Question 8: Write a program that accepts a comma separated sequence of words as input and prints
the words in a comma-separated sequence after sorting them alphabetically.
"""
input_string = raw_input("Write sequrnce of word: ")

string1 = input_string.split(",")
string1.sort()
print(str(string1)[1:-1])
