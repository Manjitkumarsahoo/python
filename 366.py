#Create a NumPy ndarray Object
#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#We can create a NumPy ndarray object by using the array() function.
#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

import numpy as np
arr=np.array([10,20,30,40])
arr1=np.array((10,20,30,40))

print(arr)
print(arr1)
print(type(arr))
