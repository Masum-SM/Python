balance = 15000
def buying_laptop(lptp_price):
    global balance # if we do not use balance as global inside fucntion we can not set global veriable(balace) inside the fucntion.we can just read the global veriable(balance))
    balance = balance - lptp_price
    print(balance)
buying_laptop(12500)

def buying_keyboard(kbrd_price):
    global balance
    balance = balance - kbrd_price
    print(balance)
buying_keyboard(2500)