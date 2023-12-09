#Access 3-D Arrays
#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

import numpy as np

arr=np.array([[[10,20,30], [40,50,60]], [[70,80,90], [100,200,300]]])

print(arr)
print(arr[0,1,2])
print(arr[1,1,2])