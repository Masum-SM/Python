
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
