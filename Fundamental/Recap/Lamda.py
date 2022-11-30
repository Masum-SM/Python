
# ---------------> EXAMPLE 01<-------------
def greed():
    print('hello every one')
greed()

# using lambda funcion
greed_ = lambda : print("hi every one")
greed_()



# ---------------> EXAMPLE 02<-------------
def max_(a,b):
    if a>b:
        return a
    else:
        return b
print(max_(6,8))

# using lambda funcion
_max = lambda a,b: a if a>b else b
print(_max(3,5))


# ---------------> EXAMPLE 03<-------------
s = 'Phitron'
new_str = lambda S : S.upper()[::-1] # start : end : step, here start and end is empty
print(new_str(s))


# ---------------> EXAMPLE 04<-------------
lst = [2,3,4,5,6,7]
def double(x):
    return x*2
for item in lst:
    print(double(item))

# using lambda function
new_lst = [lambda arg = x : arg*2 for x in lst]
for item in new_lst:
    print(item())

# ---------------> EXAMPLE 05 filter<-------------
even_list = list(filter(lambda x : (x%2 == 0),lst)) # filter return value based on specific condition.
print(even_list)


# ---------------> EXAMPLE 06 map <-------------
str_list = ['masum','nawrin','sultana','unus']
nw_str = list(map(lambda x : x.upper(),str_list)) #map work with invidual value from list one after another.
print(nw_str)


# ---------------> EXAMPLE 07 reduce<-------------
sum = 0
for num in lst:
    sum += num
print(sum)

from functools import reduce
# using lambda function
sum_ = reduce(lambda x , y : x + y , lst)
print(sum_)
