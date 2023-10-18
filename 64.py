#constructor with default parameter

class Test:
	def __init__(self,a=0,b=0,c=0):
		print("para constructor",a,b,c)
t=Test()
t1=Test(10,20,30)
t2=Test(4,5)