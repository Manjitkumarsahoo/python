#find out sum of all element from 1 to 100

from functools import reduce
data=reduce(lambda x,y:x+y,range(1,101))
print(data)
