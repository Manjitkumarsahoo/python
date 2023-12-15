#Stacking Along Height (depth)
#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

import numpy as np

arr1=np.array([10,20,30])

arr2=np.array([40,50,60])

arr=np.dstack((arr1,arr2))

print(arr)
