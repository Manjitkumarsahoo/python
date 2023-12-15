#Search sorted
#there is a method called searchsorted() which perform a binary search in an array ,and return the index where the specific value world be insert to maintain the search order .

import numpy as np

arr=np.array([6,7,8,9])

x=np.searchsorted(arr,7)

print(x)
