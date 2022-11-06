def nearly_equal(a, b):
    len_a = len(a)
    len_b = len(b)
    if(len_a<len_b):
        temp = a
        a = b
        b = temp
        temp = len_a
        len_a = len_b
        len_b = temp
    
    j = 0
    k = 0
    for i in range (len_a):
        if(a[i]==b[k]):
            k+=1
        else:
            j+=1
            if(j>1):
                break
    if(j<2):
        print(True)
    else:
        print(False)

a = input()
b = input()
nearly_equal(a, b)
