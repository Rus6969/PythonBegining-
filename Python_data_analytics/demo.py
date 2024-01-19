import folium
import pandas 

data_frame = pandas.read_csv('/Users/ruslansamatov/Projects/PythonBegining-/Python_data_analytics/volcano.csv')
Longitude = list(data_frame['Longitude'])
Latitude= list(data_frame['Latitude'])

#print(data_frame)




map = folium.Map(location=[38.58, -99.09],zoom_start=6)
fg =folium.FeatureGroup(name='my map')

for lat ,long in zip(Latitude,Longitude):
    fg.add_child(folium.Marker(location=[lat,long],popup="hi Im a volcano",icon=folium.Icon(color="green")))

map.add_child(fg)
map.save('my_volcanoMap.html')
