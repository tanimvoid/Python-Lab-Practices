import pandas as pd

series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])

# Access using indexing:
print(series['D'])

# Access using index Number:
print(series.iloc[3])