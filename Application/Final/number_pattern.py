
"""  
You need to write a python program to take an integer input from the user and print a pattern given below.									10

When n=5,
12345
21345
23145
23415
23451

"""


number = int(input("Enter a integer number: "))
for i in range(1, number+1):
    j = i
    for k in range(2, j+1):
        print(k, end='')
    print(1, end='')
    for k in range(j+1, number+1):
        print(k, end='')
    print('')
