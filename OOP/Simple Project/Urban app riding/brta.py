import random
class BRTA:
    def __init__(self) -> None:
        self.__license = {}

    def take_driving_test(self,email):
        score = random.randint(0,100)
        if score >= 33:
            # print('Congs!! You are passed.',score)
            license_number = random.randint(5000,9999)
            self.__license[email] = license_number
            return license_number
        else:
            # print('Sorry!! You are failed.',score)
            return False
    
    def validate_license(self,email,license_):
        for key,value in self.__license.items():
            if key == email and value == license_:
                return True
        return False

