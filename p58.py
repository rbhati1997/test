"""
Question 22: Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
"""

input_string = raw_input("Write string here: ")

lis2 = []
# function for calculating the frequency 
def freq(str): 
  
    # break the string into list of words 
    str_list = str.split() 
  
    # Convert list into set to remove duplicate.
    unique_words = sorted(set(str_list)) 
      
    for words in unique_words :
   
        print(words, ':',str_list.count(words)) 

# Calling function with argument.
freq(input_string)
