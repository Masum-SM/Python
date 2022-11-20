with open('File.txt','r') as f:
    pages = f.readline().split('--')
    f.close()

print(pages[0])

i = 1
page_len = len(pages)
try:
    while True:
        flag = False
        option = input("Go to next page?(enter/q to exit):")

        if option =='' or option=='q':
            flag=False
        elif option.isdigit() or option[0] == '-':
            flag = True
        else:
            flag = False

        if flag == False:
            if option == '':
                if i < page_len-1:
                    print(pages[i])
                    i +=1
                else:
                    i = i
                    print(pages[i])

            else:
                break
        else:
        
            number = int(option)
            if number > 0:
                if number < page_len-1:
                    i += number-1
                else:
                    i = 4
                print(pages[i])
                if i < page_len-1:
                    i +=1
                else:
                    i = 4
                
            else:
                break
            
except:
    print('Out of page')