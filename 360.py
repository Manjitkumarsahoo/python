import pandas as pd
import matplotlib.pyplot as plt

x=['A','B','c','d']
y=[20,30,40,90]

plt.bar(x,y,color=['r','g','b'])
plt.show()

plt.pie(y)
plt.show()