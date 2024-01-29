import pandas
import matplotlib.pyplot as plt 
from datetime import datetime

data = pandas.read_csv('/Users/ruslansamatov/Projects/PythonBegining-/Python_data_analytics/movies.csv')

group_byMethod = data.groupby(['Genre'])['Film'].count()
#print(group_byMethod)
#go specific raw 
#print(data.iloc[1:4])

print(data[['Film','Genre','Rotten Tomatoes %']].iloc[1:5])