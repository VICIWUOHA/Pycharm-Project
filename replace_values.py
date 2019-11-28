import numpy as np
import pandas as pd
from pandas import Series, DataFrame

S1 = Series([10, 20, 40, 50, 20, 10, 40, 50])
print(S1)
print(S1.replace(50, np.nan))
print(S1.replace([10, 20, 50], [100, 200, 500]))  # using array method to specify
print(S1.replace({10: 100, 20: 250, 50: np.nan}))  # using dictionary method



