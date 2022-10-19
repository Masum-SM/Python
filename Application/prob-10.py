"""  
Question : Given a string ‘s’ you need to find the words that are in list ‘a’ and use the next words on string ‘s’ to create a new string. Save it inside a file called ‘out.txt’. Remember to close the file after writing.

Write a function named create_new_string() and write your code inside this function.

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

output = "I love Bangladesh" (inside a file)

"""

with open('out.txt', 'w') as f:

    def create_new_string(a, s):
        s_list = list(s.split(' '))
        del s_list[11]
        string = ''
        for i in a:
            for j in s_list:
                if i.casefold()==j.casefold():
                  x = s_list.index(j)+1
                  string += s_list[x] + ' '
        return string


    a = ['oh', 'Emelia', 'to']
    s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
    s = s.replace(',', '')
    s = s.replace('.', '')
    string = create_new_string(a, s)
    f.write(string)
    f.close()