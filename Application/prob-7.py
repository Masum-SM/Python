"""
Question : Complete the following code (without using the replace function)-

def replace_comma_with_space(text):
    …
    …

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
"""

def replace_comma_with_space(text):
    str_list = text.split(',')
    sentence = ""
    c = 0
    for word in str_list:
        sentence += word
        if c < 8:
            sentence += " "
        c+=1
    return sentence

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)


