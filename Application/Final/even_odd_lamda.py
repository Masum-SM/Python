
""" 
QUESTION: 
You need to write a python lambda function to tell whether a number is even or not. If it is even, return “Yes” otherwise “No”.							5

print(even_odd(5))
Output:
No
"""

even_or_odd = lambda num : "Yes" if(num % 2==0) else "No"
print(even_or_odd(5))
