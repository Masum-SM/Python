
"""  
Question:
Write a python to read three floating numbers from the keyboard in a single line with ‘-’ (dash) in between and output their sum.

Example input:
>> enter numbers: 2.3-4.5-1.7

Example Output:
>> sum is: 8.5
"""

x,y,z = input("enter numbers : ").split("-")
a = float(x)
b = float(y)
c = float(z)
s = a + b + c
print("sum is : ",s)