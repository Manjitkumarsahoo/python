#Converting Data Type on Existing Arrays

import numpy as np

arr=np.array([1.1,2.1,4.9])

#newarr=arr.astype('i')
newarr=arr.astype(int)       #we can use both 'i' and 'int' 

print(arr)
print(newarr)
print(newarr.dtype)