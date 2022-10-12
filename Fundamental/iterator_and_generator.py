nums_list = [22,37,58,29,87,90,300]
numbers_iter = iter(nums_list)
try:
   print(next(numbers_iter))
   print(next(numbers_iter))
   print(next(numbers_iter))
   print(next(numbers_iter))
   print('I am exploring iteration')
   print(next(numbers_iter))
   print('I have learned moore about it')
   print(next(numbers_iter))
   print(next(numbers_iter))
   print(next(numbers_iter))
except StopIteration:
    print('iteration is stopped')