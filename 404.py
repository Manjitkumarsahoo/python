#Stacking Along Columns
#NumPy provides a helper function: vstack()  to stack along columns.

import numpy as np

arr1=np.array([10,20,30])

arr2=np.array([40,50,60])

arr=np.vstack((arr1,arr2))

print(arr)
