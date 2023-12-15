#Splitting NumPy Arrays
#Splitting is reverse operation of Joining.

#Joining merges multiple arrays into one and Splitting breaks one array into multiple.

#We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

import  numpy as np

arr=np.array([10,20,30,40,50,60,70,80,90])

newarr=np.array_split(arr,3)

print(newarr)
print(newarr[0])
print(newarr[1])
