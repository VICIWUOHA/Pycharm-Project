import pandas as pd
import seaborn as sns
from pandas import Series, DataFrame

df1 = pd.read_csv('gapminder-FiveYearData.csv')
df2 = df1.pivot('country', 'year', 'lifeExp')

# df = sns.load_dataset('gapminder-FiveYearData')
# df2 = df.pivot('country', 'lifeExp')
print(df2)

sns.heatmap(df2).get_figure().savefig('Assignment3.png')


