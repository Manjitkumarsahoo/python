#Method overriding

class Parents ():
    def show(self):
        print("Inside parent")
class Child(Parents):
    def show(self):
        super().show()
        print("Inside Child")
obj=Child()
obj.show()