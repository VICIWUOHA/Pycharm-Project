import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = pd.read_csv('demo.csv', header=None)
print(dframe)

dframe2 = pd.read_table('demo.csv', sep=',', header=None)
print(dframe2)

# # partial rules importing
# dframe3 = pd.read_csv('demo.csv', nrows=1, header=None)
# print(dframe3)
# # dumping values  or seperators
# dframe2.to_csv('outputCSV.csv', sep='!')
# # copying part of a csv file to a new file
# dframe.to_csv('dataoutput.csv', columns=[0, 2])









