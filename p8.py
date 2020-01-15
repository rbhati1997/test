"""
Question 9: Write a program that accepts sequence of lines as input and prints the lines after
making all characters in the sentence capitalized.
"""

end_with = ''
# Taking multiline input from consol/user.
input_string = '\n'.join(iter(raw_input, end_with))
print(input_string.upper())