import numpy as np
import pandas as pd
from pandas import Series, DataFrame

excel = pd.ExcelFile('demo2.xlsx')
dframe = excel.parse('demo2')
print(dframe)