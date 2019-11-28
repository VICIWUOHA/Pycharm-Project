

import pandas as pd
from pandas import Series, DataFrame

df = DataFrame({'COL1': ['uber', 'uber', 'uber', 'uber', 'grab'],
                'COL2': [5, 4, 3, 3, 5]
                })
print(df.duplicated('COL1'))
print(df.drop_duplicates())
print(df.drop_duplicates('COL1'))
print(df.drop_duplicates(['COL1'], keep="last"))



