
# ----------------------> Example 01 <----------------
lst = [[j for j in range(3)] for i in range(4)]
print(lst)
#  output : [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]




# ----------------------> Example 02 <----------------
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
