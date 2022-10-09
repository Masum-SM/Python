from re import S


def sum(*numbers):
    s = 0
    for num in numbers:
        s += num
    return s 
total = sum(1,2,3,4,5)
print(total)

def multiplication(num1,num2, *others):
    mul = 1
    for num in others:
        mul *= num
    mul *=(num1*num2) 
    print(mul)
multiplication(1,2,3,4,5)