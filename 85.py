#Abstract class

from abc import *
class Vehicle(ABC):
    def __init__(self,brand):
        self.brand=brand

    def drive(self):
        pass

class car(Vehicle):
    def drive(self):
        return f"{self.brand} car moving in the road"
    
class Motorcycle(Vehicle):
    def drive(self):
        return f"{self.brand} motercycle is speeding down the highway."


car=car("Audi")
Motorcycle=Motorcycle("TVS")

print(car.drive())
print(Motorcycle.drive())