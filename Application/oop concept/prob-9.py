""" 
Write a class with two instance variables X, n . Add two methods sum() and pow() to get the sum of X+n and exponential/power of Xn .
"""

import math
class get_solution:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num + other.num
    def __pow__(self,other):
        return math.pow(other.num,self.num)

x = get_solution(2)
n = get_solution(3)
s = x.__add__(n)
m = n.__pow__(x)
print(s)
print(m)
