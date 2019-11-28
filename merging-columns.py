import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe_1 = DataFrame({'Country': ['Nigeria', 'Uganda', 'Ghana', 'America', 'India'],
                      'Food Security Index': ['40%', '54%', '60%', '75%', '80%']})
dframe_2 = DataFrame({'Country': ['Nigeria', 'Uganda', 'Ghana', 'America', 'India', 'Russia'],
                      'Food Security Index': ['40%', '54%', '60%', '75%', '80%', '83%']})

# print(dframe_1)
# print(dframe_2)

df3 = pd.merge(dframe_1, dframe_2)
print(df3)

df4 = pd.merge(dframe_1, dframe_2, on="Country", how="right")
print(df4)

df5 = DataFrame({'Country': ['Nigeria', 'Nigeria', 'Ghana', 'Ghana', 'America', 'America', 'Nigeria'],
                 'Position': ['4th', '3rd', '1st', '2nd', '5th', '6th', '7th']})

df6 = DataFrame({'Country': ['America', 'America', 'Ghana', 'Nigeria'],
                 'Position': ['4th', '3rd', '1st', '2nd']})
print(pd.merge(df5, df6))

df7 = DataFrame({'Country': ['Nigeria', 'Nigeria', 'Uganda'],
                 'Position': ['3rd', '1st', '2nd'],
                 'FS_Index': ['60%', '80%', '75%']})

df8 = DataFrame({'Country': ['Nigeria', 'Nigeria', 'Uganda', 'Uganda'],
                 'Position': ['3rd', '3rd', '2nd', '2nd'],
                 'FS_Index': ['60%', '70%', '75%', '80%']})
print(pd.merge(df7, df8, on=['Country', 'Position'], how='outer'))

# Suffixes
print(pd.merge(df7, df8, on=['Country', 'Position'], how='outer', suffixes=('_2019', '_2020')))




