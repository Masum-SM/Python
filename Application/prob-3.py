"""  
Question:Go to this repo: https://pypi.org/project/pyjokes/ and try to make a chat bot to tell you joke using pyjokes.
Write a function named tell_some_jokes() and write your code inside this function.

"""
import pyjokes
def tell_some_jokes():
    def listen():
        return input("Want listen a Joke!!(yes/no)? : ")

    def process(command):
        words_in_small = command.lower()
        words = words_in_small .split(" ")

        for word in words:
            if  word == "no":
                return "bye"

            else:
              reply =  pyjokes.get_joke(language='en', category='all')
              return reply

    while True:
        command = listen()
        res = process(command)
        if res == 'bye':
            print("Chatbot : Bye")
            break
        else:
            print("Chatbot : ",res)

tell_some_jokes()