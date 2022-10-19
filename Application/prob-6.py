""" 
Question :  Complete the following code
def clean_string(text):
    ....
    ....
    print(output)
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)

If you face any errors, fix them. Get help from google. Do not ask others.

"""

def clean_string(text):
    sentence = ""
    for alphabet in text:
        if alphabet >= 'A' and alphabet <= 'Z' or alphabet >= 'a' and alphabet<='z':
            sentence += alphabet
    return sentence

    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)