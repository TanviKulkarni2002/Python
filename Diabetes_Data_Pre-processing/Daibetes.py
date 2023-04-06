from asyncio import as_completed
import pandas as pd
df = pd.read_csv('diabetes.csv')
#print(df.shape)
#print(df.isnull().sum())
df['Age_calculations']=(df['Age']-df['Age'].min())/(df['Age'].max()-df['Age'].min())
print(df.head(5))