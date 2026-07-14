# OOPs in Python
class Car:
    def __init__(self, name):  # Constructor
        self.name = name
    
    def showName(self):
        print(self.name)

car_1 = Car("Supra")
car_1.showName()
