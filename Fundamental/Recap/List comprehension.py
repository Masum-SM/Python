
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


# ------------------------> Example 04 : sequence of even number <------------------------

num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]

even = [n for n in num_lst if n%2 == 0]
print(even)

even_range = [n for n in range(1,16) if n%2 == 0]
print(even_range)

"""  
output : 
[2, 4, 6, 8, 10, 12, 14]
[2, 4, 6, 8, 10, 12, 14]
"""


# ------------------------> Example 05 : sequence of even number <------------------------

d_by3_5 = [num for num in range(100) if num%3 ==0 if num%5 == 0]
print(d_by3_5)
# output : [0, 15, 30, 45, 60, 75, 90]


# ------------------------> Example 06 : even and odd <------------------------

even_odd = ['even' if num%2 == 0 else 'odd' for num in range(10)]
print(even_odd)

# output : ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']


# ------------------------> Example 07 : make pair form two list <------------------------

pair = [(x,y) for x in [1,2,3] for y in [5,6,7]]
print(pair)

# output : [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
