import random
class BRTA:
    def __init__(self) -> None:
        self.__license = {} 
        # creating a dictionary of key = email and value = license_number
        
    def take_driving_test(self,email):
        score = random.randint(0,100)
        if score >= 33:
            print(f"congrats!! you {email} have passed, your score is : {score}")
            license_number = random.randint(5000,9999)
            self.__license[email] = license_number
            return license_number
        # else:
        #     # print(f"sorry you {email} have failed, your score is {score}")
        #     return False
        
    def validate_license(self, email, license):
        for key, value in self.__license.items():
            if key == email and value == license:
                return True
        return False