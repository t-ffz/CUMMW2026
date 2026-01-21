import pandas as pd

df = pd.read_csv('t2data.csv')

print(df)

col_names = df.select_dtypes(include=['float64', 'int64']).columns
df[col_names] = (df[col_names] - df[col_names].mean())/df[col_names].std()

print(df) 
