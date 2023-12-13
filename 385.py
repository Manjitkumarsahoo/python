#Copy of an array
#The copy SHOULD NOT be affected by the changes made to the original array.
import numpy as np

arr=np.array([10,20,30,40])
x=arr.copy()

arr[0]=53

print(arr)
print(x)