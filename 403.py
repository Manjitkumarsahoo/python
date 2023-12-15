#Stacking Along Rows
#numpy provides a helper function: hstack() to stack along rows

import numpy as np

arr1=np.array([10,20,30])

arr2=np.array([40,50,60])

arr=np.hstack((arr1,arr2))

print(arr)
