import pandas as pd

data = pd.Series([100, 200, 300, 400], index=['a', 'b', 'c', 'd'])

df = data.to_frame(name = 'Values')

print(df.iloc[2])

print(df.loc['c'])