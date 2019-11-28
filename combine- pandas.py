import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([5, np.nan, 6, np.nan], index=['A', 'B', 'C', 'D'])
s2 = Series(np.arange(4), dtype=np.float64, index= s1.index)

print(s2)

s3 = Series(np.where(pd.isnull(s1), s2, s1), index=s1.index )# loops throgh and replaces null s1values with s2 ands3 values
print(s3)
s4 = s1.combine_first(s2)
print(s4)
