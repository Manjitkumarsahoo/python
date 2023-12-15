#Iterate on the elements of the following 3-D array:

import numpy as np

arr=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,200,300]]])

for x in arr:
    for y in x:
        for z in y:
            print(y)