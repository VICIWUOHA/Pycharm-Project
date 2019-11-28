import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# used for rearranging rows and columns of Data
df_1 = DataFrame(np.arange(8).reshape(2, 4), index=pd.Index(['Nigeria', 'South Africa'], name='Country'),
                 columns=pd.Index(['2014', '2015', '2016', '2017'], name="Years"))

print(df_1)

# Stacking an array of data
stack_df_1 = df_1.stack()
print(stack_df_1)

unstackdf_1 = stack_df_1.unstack()
print(unstackdf_1)

df_2 = stack_df_1.unstack('Country') # indexes change to columns , columns to rows_ imdex
print(df_2)

df_3 = stack_df_1.unstack('Years')
print(df_3)

s1 = Series([5, 10, 15], index=['Nigeria', 'S.A', 'L.A'])
s2 = Series([10, 20, 30], index=['Nigeria', 'S.A', 'L.A'])

s3 = pd.concat([s1, s2], keys=['2019', '2020'])
print(s3)

s4 = s3.unstack()
print(s4)

print(s4.stack(dropna=False))
