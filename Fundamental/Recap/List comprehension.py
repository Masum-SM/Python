
# ------------------------> Example 01 : upper case <------------------------

str_list = ['masum','nawrin','sultana','unus']
new_lst = [x.upper() for x in str_list ]
print(new_lst)

# output : ['MASUM', 'NAWRIN', 'SULTANA', 'UNUS']


# ------------------------> Example 02 : sequence of number <------------------------

x = [i for i in range(1,10)]
print(x)
y = list(range(1,10))
print(y)

""" 
output : 
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9] 
"""


# ------------------------> Example 03 : sequence of alphabet <------------------------

s = 'Nawrin'
l = [a for a in s]
print(l)

print(list(s))

"""  
['N', 'a', 'w', 'r', 'i', 'n']
['N', 'a', 'w', 'r', 'i', 'n']
"""
