numbers = [36 , 67 , 74 , 56 , 40 ,68 , 87]
numbers.append(100) #insert in last of list
print(numbers)
numbers.insert(2,200) #insert in specific index in list
print(numbers)
numbers.remove(200) #Remove the first item(value) from the list whose value is equal to x.
print(numbers)
numbers.pop(3)#Remove the item at the given position in the list
print(numbers)
print(numbers.count(40)) #Return the number of times x appears in the list.
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)