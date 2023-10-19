# Multilevel inheritance

class shape:
    def __init__(self,color):
        self.color=color
    def getcolor(self):
        return self.color

class circle(shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius

    def area(self):
        return 3.14 * self.radius *self.radius
    
class coloredcircle(circle):
    def __init__(self,color,radius):
        super().__init__(color,radius)

    def display(self):
        print(f"A {self.getcolor()} circle with radius {self.radius}")

shape_obj=shape("Black")
circle_obj=circle("red",5)
colored_circle_obj=coloredcircle("Blue",3)

print("shape color:",shape_obj.getcolor())
print("Circle area:", circle_obj.area()) 
colored_circle_obj.display()             
