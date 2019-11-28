import numpy as np
import pandas as pd
from numpy import random
from pandas import Series, DataFrame
B1 = np.arange(25).reshape(5, 5)
B2 = random.randn(25).reshape(5, 5)

print(B1)
print(B2)

print('Output of the concatenated data frames are; ')
# print(np.concatenate([B1,B2], axis=1))

print(np.concatenate([B1,B2], axis=0))

S1 = Series([100, 200, 300, 400], index=['Nigeria', 'Ghana', 'Uganda', 'Cameroun'])
s2 = Series([500, 600], index=['Kenya', 'Egypt'])

print(pd.concat([S1, s2]))
print(pd.concat([S1, s2], axis=1)) # axis=1 here specifies that it shouldbe concatenated along columns

df1 = DataFrame(random.rand(4, 4), columns=['NGA', 'USA', 'CHI', 'ESP'])
df2 = DataFrame(random.rand(3, 3), columns=['USA', 'ANG', 'NGA'])

print(pd.concat([df1, df2], ignore_index=True))



