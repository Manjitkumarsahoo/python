#Abstract method (find sideds of shape)

from abc import *
class polygon(ABC):
    def noofsides(self):
        pass

class Triangle(polygon):
    def noofsides(self):
        print("I have 3 sides")

class pentagon(polygon):
    def noofsides(self):
        print("I have 5 sides")

class Xexagon(polygon):
    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(polygon):
    def noofsides(self):
        print("I have 4 sides")

T=Triangle()
T.noofsides()

P=pentagon()
P.noofsides()

X=Xexagon()
X.noofsides()

Q=Quadrilateral()
Q.noofsides()