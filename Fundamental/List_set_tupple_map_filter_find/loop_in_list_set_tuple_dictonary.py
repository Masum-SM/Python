numbers_list = [36 , 67 , 74 , 56 , 40 ,68 , 87]

numbers_set = {36 , 77 , 34 , 60 , 46 ,68 , 87}

numbers_tupple = 36 , 17 , 84 , 60 , 46 ,48 , 87

marks = {'Math':12, 'Physics':23,'Chemistry':26,'Biology':22}


""" 
list_sum = sum(numbers_list)
print(list_sum)

set_sum = sum(numbers_set)
print(set_sum)

tupple_sum = sum(numbers_tupple)
print(tupple_sum)
dictonary_sum = sum(marks.values())
print(dictonary_sum) 
"""

# ========================== sum of list ==========================
list_sum = 0
for num in numbers_list:
    list_sum += num
print(list_sum)
print("\n")


# ========================== sum of set ==========================
set_sum  = 0
for num in numbers_set:
    set_sum += num
print(set_sum)
print("\n")


# ======================== sum of tupple ========================
tupple_sum = 0
for num in numbers_tupple:
    tupple_sum  += num
print(tupple_sum)
print("\n")


# ======================= sum of dictonary =======================
dictonary_sum = 0
for num in marks.values():
    dictonary_sum += num
print(dictonary_sum)
print("\n")


# =============== Dictonary keys & values ================
for mark in marks:
    val = marks[mark]
    print(mark,val)
print("\n")


# =============== Dictonary keys & values ================
for sub, mark in marks.items():
    print(sub,mark)
print("\n")


# =============== index & values ================
for indx,num in enumerate(numbers_list):
    print(indx,num)
print("\n")