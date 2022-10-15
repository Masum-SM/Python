""" 
Question: Create a string out of some words given in a list -

l = ["This", "is", "very", "fantastic"]
Expected Output:
"This is very fantastic"
Write a function named create_string() and write your code inside this function.
"""
l = ["This", "is", "very", "fantastic"]

def create_string(li):
    string = " "
    sentence = string.join(li)
    return sentence

print(create_string(l))




