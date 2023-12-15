#Spliting 2-D Arrays

import numpy as np

arr=np.array([[10,20],[30,40],[50,60],[70,80]])

newarr=np.array_split(arr,3)

print(newarr)
