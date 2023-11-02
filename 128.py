#find the sum of all element present inside list usinf lambda

from functools import reduce
l=[1,2,3,4,5]
data=reduce(lambda x,y:x+y,l)
print(data)