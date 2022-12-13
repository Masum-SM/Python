
"""  
If any chances to found error in our code then we use try except method.
In Try part , we write our desigerd code and except part, we print possible error name.if any error found then it print except part.

we can use another two keyword with try and except those are else and finally.
else-when the code did not show any error then the else part will appear.
Finally- the finally part always runnded, if error found or not.
"""


# ---------------------------------> Example - 01 <---------------------------------------
try:
    x = 6/0
    print(x)

except:
    print('Found error.')
else:
    print('No error found.')
finally:
    print('finally will always printed.')

""" 
output: 
Found error.
finally will always printed.
"""



# ---------------------------------> Example - 02 <---------------------------------------
try:
    x = 6/2
    print(x)

except:
    print('Found error.')
else:
    print('No error found.')
finally:
    print('finally will always printed.')
