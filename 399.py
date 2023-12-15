#Iterate through every scalar element of the 2D array skipping 1 element:

import numpy as np

arr=np.array([[10,20,30,40],[50,60,70,80]])

for x in np.nditer(arr[:,::2]):
    print(x)