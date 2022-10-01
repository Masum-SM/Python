name = input("Enter your name : ")
print(name);
print(type(name));

age = input("Enter Your age : ")
print(age);
print(type(age));

""" 
When we take an input , it automatically take string type.
For number, we need to chage it number(int)
"""

num1 = input("Enter 1st number : ")
num2 = input("Enter 2nd number : ")

ans = int(num1) +int(num2)
print(ans)
print(type(ans))