numbers = [36 , 67 , 74 , 56 , 40 ,68 , 87]
print(numbers[0])
print(numbers[-1])
# NOTE : array or list start from 0 index from left side goes to right and start from -1 from right side goes to left.

print(numbers[1:5]) # we can access from specific range from list.here it starts from 1 and print before 5th index.
print(numbers[3 : ])# start from 3 print to the last.
print(numbers[3:-1])# print from 3 to before last index.cz -1 is last index
print(numbers[2 : 7 : 2])# print from 2nd index to 7th index after passing 2 value.
print(numbers[7:2:-1])#print from 7th to 2nd index in right to left.
print(numbers[-2:-8:-2])
print(numbers[:])#print all list left to right
print(numbers[: : -1])#print all list right to left