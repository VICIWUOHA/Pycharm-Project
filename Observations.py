import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.random.randn(1000, 5))
print(df)

# when observing a dataframe start with df.head
print(df.head())  # prints first 5 rows from top
print(df.tail())  # prints last 5 rows
print(df.describe())  # gives count, avg, percentage of each column, like descriptive stats

column = df[0]
print(column.head())

