with open('File.txt','r') as f:
    pages = f.readline().split('--')
    f.close()

print(pages[0])

i = 1
page_len = len(pages)
while page_len-1:
    option = input("Go to next page?(enter/q):")
    if option == '':
        print(pages[i])
        i +=1
        page_len -=1
        
    else:
        break
        

        
 

