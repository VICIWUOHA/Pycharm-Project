import numpy as np
import pandas as pd
from pandas import Series, DataFrame, read_html

# how to read table data from a remote repository
url = "https://countrycode.org/"
dflist = pd.io.html.read_html(url)
dframe = dflist[0]
print(dframe)

print(dframe.columns.values)


