#DataFrames

#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#Series is like a column, a DataFrame is the whole table.

import pandas as pd

data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}

x=pd.DataFrame(data)

print(x)

print(x.loc[0])
print(x.loc[[0,1]])