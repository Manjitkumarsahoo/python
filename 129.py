#Find the product off all element present in side list with using lambda

from functools import reduce
l=[1,2,3,4,5]

data=reduce(lambda x,y:x*y,l)

print(data)