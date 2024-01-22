import pandas
import matplotlib.pyplot as plt 
from datetime import datetime

data = pandas.read_csv('/Users/ruslansamatov/Projects/PythonBegining-/Python_data_analytics/movies.csv')
#print(data)
#print("########################")
#print(data['Film'])

#print(data.head())

#print(data.shape)

#print(data.hist('Year'))

plt.show()


 # get specific row
print(data.at[2,'Worldwide Gross'])

#search base on condidtion 
print(data[data['Rotten Tomatoes %']>90])

# how many movies like that >90 
print(data[data['Rotten Tomatoes %']>90].count())


#1 
d2 = data[data['Rotten Tomatoes %']>90]
print("***********************************************************")
#multiple condition tomatoes more 80 and genere comedy 
dataFrame_multiple = data[(data["Rotten Tomatoes %"]>80) & (data["Genre"]=='Comedy')]

print(dataFrame_multiple) 
#Time based filtering 
# data_filttered =data[(data["Year"] > datetime(2020,11,11)) & (data["Year"] < datetime(2022,12,31))]
# print("++++++++++++++++++++++++++++++++++++++++++++++")
# print(data_filttered)

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# FROM DATA to information average rating for 
average_rating = data[data['Rotten Tomatoes %']==90].mean()
print(average_rating)
print("*******************************************")
#groupBY 

Group_By = data.groupby(['Genre'])['Film'].count()
print(Group_By)

#plt.pie(Group_By)
plt.show()

#give a label 
plt.pie(Group_By,labels=Group_By.index)
plt.show()