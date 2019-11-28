import pandas as pd
import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds1 = randn(1000)
ds2 = randn(100)

plt.hist(ds1)
plt.savefig('hist_1.png')
# plt.show()

plt.hist(ds2)
plt.savefig('hist_2.png')
# plt.show()


plt.hist(ds1, density=True, color='red', bins=15, alpha=0.5)
plt.hist(ds2, density=True, label='Testing Histograms', bins=15, alpha=0.5)
plt.savefig('hist_3.png')
# plt.show()

ds3 = randn(1000)
ds4 = randn(1000)

sns_plot = sns.jointplot(ds3, ds4)  # gives a scatter plot
sns_plot.savefig('sns_plot4.png')


sns_plot_2 = sns.jointplot(ds3, ds4, kind='hex')  # Hexagon kinda heat map
sns_plot_2.savefig('sns_plot5.png')
