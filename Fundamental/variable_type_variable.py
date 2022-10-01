""" 
In pytho, To declare a variale 3 things are neede.
 * varialbe_name.
 * assignment_Operatior ( = ).
 * value for variable.
"""

# ===================>  NUMBER <====================
num1 = 20;
num2 = 5;
print(num1 + num2)

num3 = 10.4
num4 = 0.6
print(num3 + num4)
print(num1 + num3)

# ===================>  STRING <====================
first_name = "Unus"
last_name = "Masum"
full_name = first_name + ' '+last_name
print(full_name)

sentence = "My name is Masum. \nI am 26 years old.\nI am studing in Computer Science."
print(sentence)

# DYNAMIC  String (called f string)
age = 26
about_me = f'My name is {full_name} and I am {age} years old'
print(about_me)
# ===================>  BOOLEAN <====================
is_okey = True

# ===================>  TYPE <====================
# The type keyword provide the type of variable.
print(type(full_name))
print(type(age))
print(type(is_okey))