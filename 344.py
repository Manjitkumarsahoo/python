import pandas as pd

data={
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

x=pd.DataFrame(data,index=["day1","day2","day3"])
print(x)
print(x.loc["day2"])
