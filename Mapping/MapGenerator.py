import folium
import geopy
import pandas

data=pandas.read_csv("ProjList.csv",sep=";",error_bad_lines=False)

map = folium.Map(location=[-30.5,22.9], zoom_start=6)
# map.add_child(folium.Marker(location=[-30.5,22.9],popup="This is the starting point", icon=folium.Icon(color='blue')))
fg= folium.FeatureGroup(name="My Map")

#Extract the coordinates from the csv file
datakeys = data.keys()
for i in datakeys :
    print(i)
coordinates = data["Location"]
names = data["Client"]

#CData = data["Client"] + ";" + data["location"]
CData = zip(data["Index"],data["Client"],data["Location"])


#need to update the popup function to select the correct naem of the company/mine
def CreateMarkers(coordinates):
    for i in coordinates:
        if len(str(i)) > 3:
            POI=geopy.Point(i)
            fg.add_child(folium.Marker(location=[POI.latitude,POI.longitude],popup="This is the starting point", icon=folium.Icon(color='blue')))
            map.add_child(fg)

#For markers it is easier to create a feature gorup variable to control the look of the icon markers

#fg.add_child(folium.Marker(location=[-30.5,22.9],popup="This is the starting point", icon=folium.Icon(color='blue')))
#map.add_child(fg)
CreateMarkers(coordinates)
map.save("MapMarked.html")
