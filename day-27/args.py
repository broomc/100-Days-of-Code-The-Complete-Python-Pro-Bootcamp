def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    
    print(sum)
#add(1,2,3,4,5)

def calculate(n, **kwargs):
    #for key,value in kwargs.items():
    #    print(key)
    #    print(value)
    
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
        

my_car = Car(make="Nissan")#, #model="GT-R")

print(my_car.make)
print(my_car.model)
