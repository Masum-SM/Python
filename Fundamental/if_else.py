num1 = 6
num2 = 40
num3 = 30

if num1 > num2 and num1 > num3:
    print(f'num1 = {num1} is grater number.')
elif num2> num1 and num2 > num3:
    print(f'num2 = {num2} is grater number.')
else:
    print(f'num3 = {num3} is grater number.')

if num1 > 10 or num1 > 3 *3:
    print(f'{num1} contain more than one digit')
else :
    print(f'{num1} contain single one digit')

if( num3 > num1):
    if(num3 > num2):
        print("Yes")
    else:
         print("No")