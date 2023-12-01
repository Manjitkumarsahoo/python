#Create Label
import pandas as pd

a=[10,20,30,40]

x=pd.Series(a,index=["x","y","z","m"])

print(x)

print(x["z"])