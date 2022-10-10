try:
    num = 11/0
    print(num)
except:
    print('Something went wrong')
finally:
    print('This is done')