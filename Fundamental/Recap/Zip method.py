
# ---------------------------------- Example 01 -------------------------

nums = (1,2,3)
string = ['one','two','three']
num = [1.1,2.2,3.3]

new_obj = zip(nums,string,num)
print(list(new_obj))
# output : [(1, 'one', 1.1), (2, 'two', 2.2), (3, 'three', 3.3)]



# ---------------------------------- Example 02 -------------------------

names = ['masum','karim','halim']
salaries = [10000,20000,30000]
print(list(zip(names,salaries)))
# output : [('masum', 10000), ('karim', 20000), ('halim', 30000)]


new_dct = {name:salary for name,salary in zip(names,salaries)}
print(new_dct)
# output : {'masum': 10000, 'karim': 20000, 'halim':


result = list(zip(names,salaries))
name,salary = zip(*result)
print(name) # output : ('masum', 'karim', 'halim')
print(salary) # output : (10000, 20000, 30000)
