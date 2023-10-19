
#Hybrid inheritace

class A:
	def __init__(self):
		super().__init__()
		print("AC")	
class B(A):
	def init(self):
		print("BC")
		super().__init__()
class C:
	def __init__(self):
		print("CC")
class D(B,C):
	def __init__(self):
		super().__init__()
		print("DD")
ob=D()