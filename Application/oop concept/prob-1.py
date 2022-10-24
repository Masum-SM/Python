"""  
Questions:
Create a function exp(a, n) that returns the exponential result ( an ). Read user input a and n in a single line from the keyboard.

Example input:
>> enter numbers: 2 3

Example Output:
>> result is: 8


"""

import math
def exp(a,n):
    return math.pow(a,n)

x, y = input("Enter numbers: ").split()
a = int(x)
n = int(y)

res = exp(a,n)
print("result is: ",int(res))