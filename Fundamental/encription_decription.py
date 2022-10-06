data = "masum"
shift = 7
encripted_str = ""
decripted_str = ""
for char in data :
    encripted_str += chr((((ord(char)+shift)-97)%26)+97)
print(encripted_str)

for char in encripted_str:
     decripted_str += chr((((ord(char)-shift)-97)%26)+97)

print(decripted_str)