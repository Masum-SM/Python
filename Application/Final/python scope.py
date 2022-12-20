""" There are four types of scopes in python
Local Scope: A variable that is inside a function is determined as local scope of that function, and we can not access that varible outside the function. 

Global Scope: A variable that is in the main body of the Python code is a global variable and belongs to the global scope. It is possible to access global variable at anywhere from the program.

Built-in Scope: Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session.
Enclosing Scope: Enclosing function can exists for nested function and it is special type of scope.
 """

from math import e
print(e) #build_in scope
e = 33.23 # global scope
def outer_fun():
    e = 43.36 # outer_fun local scope 
    def inner_fun():
        e = 77.98 #inner_fun enclosed scope.
        print(e)
    inner_fun()
outer_fun()
print(e)
