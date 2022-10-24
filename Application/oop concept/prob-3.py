"""  
Question:
Write a python program to reverse every word from a given string s and output a new string. The position of words will remain the same, but their contents will be in reverse order.

s = “Programming Hero is the best”

Expected output: “gnimmargorP oreH si eht tseb”
"""

s = "Programming Hero is the best"
word_list = s.split()

rev_s = ""
for i in word_list:
    rev_s = rev_s + ' ' + i[::-1]
print(rev_s.lstrip()) 