# -------------------------------------------- OOPs in Python -------------------------------------------------

class Car:

    wheels = 4                 # Class variable

    def __init__(self, name):  # Constructor
        self.name = name       # Instance Variable
    
    def showName(self):
        print(self.name)

    def start(self):
        print(self.name + " has started")

car_1 = Car("Nissan_Skyline")
car_2 = Car("Supra")
# car_1.showName()
# car_2.showName()
# car_1.start()


# -----Inheritance-----

class Animal:
    def alive(self):
        print("Yeah the animal is alive")

class Dog(Animal):
    pass
class Cow(Animal):
    pass

dog = Dog()
#dog.alive()

cow = Cow()
#cow.alive()

# -----Multiple Inheritance-----
class A:
    def parent1(self):
        print("Class A")
class B:
    def parent2(self):
        print("Class B")
class C(A, B):
    pass
c = C()
# c.parent1()
# c.parent2()


# -----Higher Order Function-----

def up(text):
    return text.upper()

def hello(func):
    text = func("Hello")
    print(text)

hello(up)       # accepts a function as an argument

def divisor(x): # returns a function
    def dividend(y):
        return y / x
    return dividend

divide = divisor(5)
# print(divide(10))


# -----lambda function-----
double = lambda x : x*2
volume = lambda x, y, z : x*y*z
full_name = lambda first, last : first + " " + last
enter_or_not = lambda age : True if age >=18 else False

print(double(5))
print(full_name("Elon", "Musk"))
print(enter_or_not(15))