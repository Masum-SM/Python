class phone:
    manufactures = 'china'
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def send_sms(self,number,text):
        sms = f"Sending {text} to {number}"
        print(sms)

my_phone = phone("onePlus","Blue",38000)
print(my_phone.manufactures)
print(my_phone.brand,my_phone.color,my_phone.price)
bro_phone = phone("iPhone","see_green",1500000)
print(bro_phone.brand,bro_phone.color,bro_phone.price)
print(my_phone.price,bro_phone.price)