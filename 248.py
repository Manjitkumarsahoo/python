#predefined function
#triu() upper triangular matrix

import numpy as np
A=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
A=np.triu(A) 
print(A)
