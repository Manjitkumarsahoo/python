#Abstract methiod (find the area of shape)

from abc import *
class shape(ABC):
    def calculate_area(self):
        pass

class Circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return 3.14*self.radius*self.radius
    
class Rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length * self.width
    
Circle=Circle(5)
Rectangle=Rectangle(4,5)

print(f"Area of the circle: {Circle.calculate_area()}")
print(f"Area of the rectangle: {Rectangle.calculate_area()}")
