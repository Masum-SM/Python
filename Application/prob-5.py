""" 
Question:You have given a dictionary ‘d’, convert it into a list. The first value will be the key of the dict, and value will come next. 
Example
x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
output:  [ 'a', 1, 'b',  2, 'c', 3, 'd', 4]

Now do the same for -
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
Write a function named create_list() and write your code inside this function.
"""
def create_list(d) :
    my_list = []
    [my_list.extend([k,v]) for k,v in d.items()]
    print(my_list)
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
create_list(d)