# with open('message.txt','w') as fw:
#     fw.write('Iove python.')

# with open('message.txt','a') as fw:
#     fw.write('\nSo I am learning python.')

with open('message.txt','r') as fr:
    text = fr.read()
    print(text)