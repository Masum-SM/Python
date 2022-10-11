numbers = [36 , 67 , 74 , 56 , 68, 40 ,68 , 87]
num = {22,33,44,77,55,22,66}
print(numbers)
print(num)
# we can not hold duplicate in set, it contain only unique value. there is no specific order

numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(77)
print(numbers_set)

numbers_set.remove(56)
print(numbers_set)
print(len(numbers_set))