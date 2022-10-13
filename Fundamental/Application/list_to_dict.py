my_list = ['@F1','RBRC','!3','@F2','WBSC','@F3','&ayc','MBRN','@F4','$nvy@','SBMC','@F5','QXRI']

# Expected: {'@F1','RBRC','@F2','WBSC','@F3','MBRN','@F4','SBMC','@F5','QXRI'}

list_len = len(my_list)
output_dict ={}

for indx,val in enumerate(my_list):
    if val[0] == '@':
        output_dict[val] = my_list[indx+1]
print(output_dict)