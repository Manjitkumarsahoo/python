#Multiplication of array
#the number of columns in the first matrix (A) must be equal to the number of  rows in the second matrix (B)


import numpy as np
A=np.matrix([[1,2,3],[4,5,6]])
B=np.matrix([[1,2],[3,2],[4,5]])

C=A*B
print(C)
