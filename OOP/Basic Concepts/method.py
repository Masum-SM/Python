class phone:
    brand = "OnePlus"
    price = 38500
    features = ["Quared camra","5G","Ram:12GB","Rom:256GB"]

    #==================== Method===============
    def call(self,number):
        print(f"Calling to {number}")

    def sms(self,number,text):
        return f"Sending {text} to {number}"

onePlus = phone()
onePlus.call("0152112030")
print(onePlus.sms("0132849632","Please come early"))