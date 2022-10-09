""" 
key value arguments
"""

def fullName(**kargs):
    print(kargs)
fullName(f_name='Md.',m_name ='Unus',l_name='Masum')
print("\n\n")
def mixName(first,last,**other):
    print(first,last,other)
mixName(first='Md.',last='Masum',middle='Unus')
print("\n\n")
def allTypes(first,*args,**kargs):
    print(first)
    print(args)
    print(kargs)
allTypes('Md.','Unus','Masum',sirName='Patwary')
print("\n\n")
def all_types(first,*args,**karg):
    print(first)
    for word in args:
        print(word)
    print(karg)
    for key,value in karg.items():
        print(key,value)

all_types('abc','aaa','ccc','ddd',f_name='Unus',l_name='Masum')
print("\n\n")