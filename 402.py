#Joining Arrays Using Stack Functions
#Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

#We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

#We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

import numpy as np

arr1=np.array([10,20,30])
arr2=np.array([40,50,60])

arr=np.stack((arr1,arr2),axis=1)

print(arr)

