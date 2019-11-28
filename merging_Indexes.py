import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df_1 = DataFrame({'State': ['Abia', 'Edo', 'Lagos', 'Abia', 'Edo'],
                  'Data': range(5)})
print(df_1)

df_2 = DataFrame({'Profit': [100, 200]},
                 index=['Abia', 'Edo'])
print(df_2)

print(pd.merge(df_1, df_2, left_on='State', right_index=True))

# Join function

print(df_1.join(df_2))
