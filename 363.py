import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
sns.barplot(x='Duration',y='Maxpulse',data=df)
print(plt.xticks(rotation=60))
print(plt.show())