
class user:
    def __init__(self,name,roll,password):
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.return_books = []

class Libary:
    def __init__(self,book_list):
        self.book_list = book_list

    def borrow_book(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print("Please return book.")
                    return
                if self.book_list[book] == 0:
                    print("Book quantity is Zero, Come latter")
                    return
                self.book_list[book] -=1
                user.borrow_books.append(bookName)
                print(f"You have borrowed {bookName}")
                return
        print("Book not available in Libary")

    def return_books(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if book in user.borrow_books:
                    self.book_list[book] +=1
                    user.borrow_books.remove(bookName)
                    user.return_books.append(bookName)
                    print("Book return successfully")
                    return
                else:
                    print(f"{bookName} is not availabe in your borrowed list.")
        print("Not our book.")

    def availability(self):
        for book in self.book_list:
            if self.book_list[book] >0:
                print(book,self.book_list[book])

    def donate_book(self,bookName,amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print("Thanks for donating.")
                return
        self.book_list[bookName] = amount
        print("Thanks for donating.")

libary = Libary({"English":3,"Bangla":4,"Math":7})
allUsers = []
currentUser = None

while True:
    if currentUser == None:
        print("Not logged in \nPlease Register or Login (R/L)")
        option = input()
        if option == "L":
            roll = input("Roll: ")
            password = input("Password : ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("No user found")
        else:
            name=input("Name : ")
            roll = input("Roll : ")
            password = input("Password : ")
            found = False
            for user in allUsers:
                if roll == user.roll:
                    
                    found = True
            if found:
                print("Account is already created.")
                continue

            user = user(name,roll,password)
            currentUser = user
            allUsers.append(user)
    else:

        print("\n\nOptions")
        print("________")
        print("1. Borrow a book.")
        print("2. Return a book")
        print("3. Borrowed book list.")
        print("4. Return book list.")
        print("5. Check availabe book.")
        print("6. Donate a book.")
        print("7. Logout.")
        x = int(input("Give Option : "))
        if x == 1:
            bookName = input("Book name : ")
            libary.borrow_book(bookName,currentUser)
        elif x == 2:
            bookName = input("Book Name : ")
            libary.return_books(bookName,currentUser)
        elif x == 3:
            print(currentUser.borrow_books)
        elif x == 4:
            print(currentUser.return_books)
        elif x == 5:
            libary.availability()
        elif x == 6:
            bookName = input("Book name : ")
            amount = int(input("Amount : "))
            libary.donate_book(bookName,amount)
        elif x == 7:
            currentUser = None


    
