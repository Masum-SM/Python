
# ==================== filter in list ====================
numbers_list = [36 , 67 , 74 , 56 , 40 ,68 , 87]
bigger_num = filter(lambda num : num > 50,numbers_list)
print(list(bigger_num))

# ==================== filter in dictonary ================
actors = [
    {'name':'purnima','age':40},
    {'name':'sabana','age':60},
    {'name':'promoni','age':30},
    {'name':'tushi','age':25},
]

senior_actor = filter(lambda actor : actor['age']>35,actors)
print(list(senior_actor))