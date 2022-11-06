string = input()
flag = True
str_len = len(string)

for i in range(0, int(str_len/2)):
	if string[i] != string[str_len-i-1]:
		flag = False
		break
if (flag):
	print("It is a Pallindrome")
else:
	print("It not a Pallindrome")
