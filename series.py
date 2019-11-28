import numpy as np
import pandas as pd
from pandas import Series


subject = Series([5, 10, 15, 20, 25])
print(subject)

print(subject.values)
print(subject.index)
# here we used custom indexes
data_array = np.array(['a', 'b', 'c'])
s = Series(data_array, index=[100, 200, 300])
print(s)

deby_data = np.array(['Sex', 'Age', 'Revenue'])
t = Series(deby_data, index=['Row1', 'Row2', 'Row3'])
print(t)

Gdp_in_Billions = Series([20, 80, 70, 90, 200], index=['Abia', 'Imo', 'Abuja', 'Kano', 'Lagos'])
print(Gdp_in_Billions)

print(Gdp_in_Billions['Abia'])
print(Gdp_in_Billions[Gdp_in_Billions >= 80])

# to confirm if something is in the array
print('Imo' in Gdp_in_Billions)

# Generating dictionaries
Gdp_dict = Gdp_in_Billions.to_dict()
print(Gdp_dict)

# nan values - not available value
index_2 = ['Abia', 'Imo', 'Abuja', 'Kano', 'Lagos', 'Oyo']
Gdp_in_Billions_2 = Series(Gdp_in_Billions, index_2)
print(Gdp_in_Billions_2)

print(pd.isnull(Gdp_in_Billions_2))
print(pd.notnull(Gdp_in_Billions_2))

# Addition of series
print(Gdp_in_Billions + Gdp_in_Billions_2)

# Assigning names

Gdp_in_Billions_2.name = 'States GDP'
Gdp_in_Billions_2.index.name = 'State Name'

print(Gdp_in_Billions_2)



