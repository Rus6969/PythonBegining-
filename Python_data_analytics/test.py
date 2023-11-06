import folium 
import pandas
map = folium.Map(location=[38.58,-99.09],zoom_start=6)
data = pandas.read_csv("volcano.csv")
Latitude = list(data["Latitude"])
Longitude = list(data["Longitude"])
figure = folium.FeatureGroup(name="my map")

for lat, long in zip(Latitude, Longitude):
      figure.add_child(folium.Marker(location=[lat,long],popup="my location my house",icon=folium.Icon(color="green")))




map.add_child(figure)
map.save("My_first_map.html")