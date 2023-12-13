#VIEW
#Make a view, change the original array, and display both arrays:

import numpy as np

arr=np.array([10,20,30,40])

x=arr.view()
arr[0]=53

print(arr)
print(x)