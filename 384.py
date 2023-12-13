#Change data type from integer to boolean

import numpy as np

arr=np.array([1,2,3,0])

newarr=arr.astype(bool)

print(newarr)
print(newarr.dtype)