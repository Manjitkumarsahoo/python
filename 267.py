#Add multiple element in set
#using reduce 

from functools import reduce

s={10,20,30}
L=[40,50,60]

s1=reduce(lambda res, x: res.union(set([x])),L,s)

print(s1)