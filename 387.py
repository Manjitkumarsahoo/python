#Check if Array Owns its Data
#As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

#Every NumPy array has the attribute base that returns None if the array owns the data.

#Otherwise, the base  attribute refers to the original object.


import numpy as np

arr=np.array([10,20,30,40])
x=arr.copy()
y=arr.view()

print(arr)
print(x.base)
print(y.base)