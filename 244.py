#Display all lement fron an array

import numpy as np
A=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(A)
for i in A:
    for j in i:
        print(j,end="\t")
    print()

    