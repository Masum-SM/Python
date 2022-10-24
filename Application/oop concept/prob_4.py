
"""  
Question:
Write a python program for the requirement below. Notice the output must be in sorted order -
Input  : x3b4U5i2
Output : bbbbiiUUUUUxxx



"""
string = "x3b4U5i2"
string_lower = string.casefold()
list = list(string_lower)
list = {list[i]: int(list[i+1]) for i in range(0, len(list),2)}
list = dict(sorted(list.items()))

for key, val in list.items():
    
    flag = False
    for i in string:
        if i == key:
            flag = True
            break

    if flag == False:
        char = key.upper()
    else:
        char = key
    for k in range(val):
        print(char, end='', flush=True)