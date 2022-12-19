""" 
Write a python program to make the data given below using list and dictionary comprehension and print it.								10

data={1:[2,3,4,5],2:[1,3,4,5],3:[1,2,4,5],4:[1,2,3,5],5:[1,2,3,4]}

data = {}
ls = [1, 2, 3, 4, 5]
for i in ls:
    ls2 = []
    for j in ls:
        if j!=i:
            ls2.append(j)
    data[i] = ls2
print(data)

 """

data = {i+1:[j+1 for j in range(5) if j!=i] for i in range(5)}
print("data=",data)

# dct = {i+1:[j+1 for j in range(5) if j!=i] for i in range(5)}
# print(dct)
