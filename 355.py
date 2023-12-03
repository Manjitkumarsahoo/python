#Replace only for Specified columns
import pandas as pd

df=pd.read_csv('data.csv')
df["calories"].fillna(131,inplace=True)
print(df.to_string)
