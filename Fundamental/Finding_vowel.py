data = "aNtEriour\n\t>>"
data_in_lower = data.lower()
output_str = ""
for alphabet in data_in_lower :
    if (alphabet == 'a') or (alphabet =='e') or (alphabet =='i') or (alphabet =='o') or  (alphabet =='u'):
        output_str += alphabet + " "
print(output_str)
