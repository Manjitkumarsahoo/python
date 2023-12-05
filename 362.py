import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
print(df.head())
print(df.shape)
sns.lineplot(x='Pulse',y='Maxpulse')
plt.show()
