class calculator:
    features = {'name' : 'Casio','model':'fx-999'}
    def additon(self,x,y):
        print(x+y)

    def substruction(self,x,y):
        print(x-y)
    def multiplication(self,x,y):
        print(x*y)
    def division(self,x,y):
        print(x/y)

sm_cal = calculator()
print(f"Calculator name : ",sm_cal.features["name"])
print(f"Calculator Model : ",sm_cal.features["model"])

sm_cal.additon(39,47)
sm_cal.substruction(59,21)
sm_cal.multiplication(12,6)
sm_cal.division(69,3)