
# ----------------------------> Example 01 <-------------------------------
lst = [[j for j in range(3)] for i in range(4)]
print(lst)
#  output : [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]




# --------------------------------> Example 02 <-------------------------------
twoD_0_lst = [[0 for j in range(3)] for i in range(3)]
print(twoD_0_lst)
twoD_0_lst[0][1] = 1
twoD_0_lst[1][0] = 1
print(twoD_0_lst)

print(id(twoD_0_lst[0])) #1976448958784
print(id(twoD_0_lst[1])) #1976448958912

"""  
memory address is different
output
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]       
[[0, 1, 0], [1, 0, 0], [0, 0, 0]] 

"""


# -------------------------------> Example 03 <----------------------------
r,c = (3,3)
liist = [[0]*c]*r
print(liist)
liist[0][0] = 1
print(liist)

print(id(liist[0])) #2755471505280
print(id(liist[1])) #2755471505280



""" 
memory address is same
output 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]       
[[1, 0, 0], [1, 0, 0], [1, 0, 0]] 
here memory location of [0][0] , [1][1] and [2][2] is same
"""



# --------------------------------> Example 04 <----------------------------------
list_ = [[1,2,3],[4,5,6],[6,7,8]]
twoD_to_1D = [sublist for val in list_ for sublist in val]
print(twoD_to_1D)

# output : [1, 2, 3, 4, 5, 6, 6, 7, 8]


# ----------------------> Example 05 <----------------
word_list  = [['banana','mango'],['apple','jackfruit'],['goyava','grape']]
nw_lst = [sublist for val in word_list for sublist in val if len(sublist)>5]
print(nw_lst)

# output : ['banana', 'jackfruit', 'goyava']
