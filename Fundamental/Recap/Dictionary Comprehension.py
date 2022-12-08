
# ------------------------> Example 01 : dictonay for 0 to 9  <------------------------

dct = {i : i+10 for i in range(10)}
print(dct)
# output : {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}



# ------------------------> Example 02 : dictonay for even age  <------------------------

dct_name_age = {'masum':26,'nawrin':23,'afra':6,'arisha':1,'batchu':79,'shazeda':56}
even_age = {k:v for k,v in dct_name_age.items() if v % 2 == 0}
print(even_age)

# output : {'masum': 26, 'afra': 6}



# ------------------------> Example 03 : dictonay for even age and upper 20 <------------------------

even_age_older = {k:v for k,v in dct_name_age.items() if v % 2 == 0 if v > 20}
print(even_age_older)

# output:{'masum': 26}



# ------------------------> Example 04 : dictonay for younger and older <------------------------
younger_older = {k:('older' if v>50 else 'younger') for k,v in dct_name_age.items()}
print(younger_older)

# output : {'masum': 'younger', 'nawrin': 'younger', 'afra': 'younger', 'arisha': 'younger', 'batchu': 'older', 'shazeda': 'older'}




# ------------------------> Example 05 : dictonay for even age and upper 20 <------------------------

double_dct = {k1 : {k2 : k1*k2} for k2 in range(6) for k1 in range(6)}
print(double_dct)

# output : {0: {5: 0}, 1: {5: 5}, 2: {5: 10}, 3: {5: 15}, 4: {5: 20}, 5: {5: 25}}
