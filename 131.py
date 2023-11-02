#working with list which is containg srtring data
from functools import reduce
name=['Good ','mornging ','every ','one ']
data=reduce(lambda x,y:x+y,name)
print(data)