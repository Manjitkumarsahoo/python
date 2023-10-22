#Abstract class

from abc import *
class MyDemo(ABC):
	@abstractmethod
	def show(self):
		pass
class MyDemo1(MyDemo):
	def show(self):
		print("show defined")
ob=MyDemo1()
ob.show() 
