import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame({'Country': ['Afghanistan', 'Albania', 'Nigeria'],
                'Code': ['89', '345', '213']
                })
GDP_map = {'Afghanistan': '20', 'Albania': '12.8', 'Algeria': '215'}
print(GDP_map)

# Mapping values in df to values in GDP_map

df['GDP'] = df['Country'].map(GDP_map)

print(df)
