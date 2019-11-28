import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.arange(25).reshape(5, 5), index=['ABIA', 'IMO', 'ONDO', 'LAGOS', 'ABUJA'],
               columns=['Income', 'Loss', 'GDP', 'Tax', 'Age'])
print(df)

# uses mapping method to rename index
df.index = df.index.map(str.lower)
# uses rename() method to rename index
print(df.rename(index=str.title, columns=str.lower))

# using dictionary method
print(df.rename(index={'abia': 'God''s'' own state'}, columns={'Income': 'Revenue'}))

# to save we add the argument inplace=True
print(df.rename(index={'abia': 'God''s'' own state'}, columns={'Income': 'Revenue', 'Loss': 'Lost Funds'}, inplace=True))
print(df)


# print(df)

