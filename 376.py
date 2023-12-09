#Slicing arrays
#Slicing in python means taking elements from one given index to another given index.

#We pass slice instead of index like this: [start:end].

#We can also define the step, like this: [start:end:step].

#If we don't pass start its considered 0

#If we don't pass end its considered length of array in that dimension

#If we don't pass step its considered 1


import numpy as np

arr=np.array([10,20,30,40,50,60,70])

print(arr[1:5])
print(arr[4:])           #slicing from index 4 to end
print(arr[:4])           #sliceing from the beginning to index 4
