#join 2-D array along rows (axis=1)

import numpy as np
arr1=np.array([[10,20],[30,40]])
arr2=np.array([[50,60],[70,80]])

arr=np.concatenate((arr1,arr2),axis=1)

print(arr)

