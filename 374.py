#Access 2-D Arrays
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
#Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

import numpy as np
arr=np.array([[10,20,30],[40,50,60]])

print(arr)
print('2nd element on 1st row :' ,arr[0,1])
print('2nd element on 2 row :',arr[1,1])
