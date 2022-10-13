


greet_word = ['hi','hlw','hello','hey','yo']
bye_word = ['bye','tata','okey']
bad_word = ['bitch','ass','dog','cat']

def listen():
    return input("Say something : ")

def decide(command):
    words_in_small = command.lower()
    words = words_in_small .split(" ")

    for word in words:
        if word in greet_word:
         talkback(word)
         break
        elif word in bye_word:
            talkback("He said bye")
            break
        elif word in bad_word:
            talkback("He is a bad person")
            break
        
            


def talkback(response):
    print(response)

command = listen()
decide(command)
