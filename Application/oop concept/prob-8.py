"""  
Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Input:
numbers= [10,20,10,40,50,60,70]
target=50 
Output: 3, 4


"""

class get_pair:
  def sum_of_pair(self, numbers, target):
       intended_pair = {}
       for i, num in enumerate(numbers):
           x = target - num
           if x in intended_pair:
               return (intended_pair[x], i )
           intended_pair[num] = i

numbers= [10,20,10,40,50,60,70]
target=50        
result = get_pair().sum_of_pair(numbers,target)
print(f"Output : {result[0]+1} , {result[1]+1}")
