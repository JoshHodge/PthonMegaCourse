import folium
import geopy
import pandas
import xml.etree.ElementTree as xml
import networkx as nx

data=pandas.read_csv("ProjList.csv",sep=";",error_bad_lines=False)

#map = folium.Map(location=[-25.5,22.9], zoom_start=5,tiles='CartoDB dark_matter')
map = folium.Map(location=[-25.5,22.9], zoom_start=5,tiles='http://tile.stamen.com/toner/{z}/{x}/{y}.png', attr='"Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>."')
#mapRail = folium.Map.add_child(location=[-30.5,22.9], zoom_start=6, tiles='http://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png', attr="<a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>, Style='<a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA 2.0</a> <a href='http://www.openrailwaymap.org/'>OpenRailwayMap</a> and OpenStreetMap")
#Style: <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA 2.0</a> <a href="http://www.openrailwaymap.org/">OpenRailwayMap</a> and OpenStreetMap
#tiles='CartoDB dark_matter'
#tiles good black and white http://tile.stamen.com/toner/{z}/{x}/{y}.png
#tiles="'http://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png'", attr="<a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors</a>"
# map.add_child(folium.Marker(location=[-30.5,22.9],popup="This is the starting point", icon=folium.Icon(color='blue')))
fg= folium.FeatureGroup(name="My Map")

#Extract the coordinates from the csv file
datakeys = data.keys()
for i in datakeys :
    print(i)

coordinates = list(data["Location"])
names = list(data["Client"])

#CData = data["Client"] + ";" + data["location"]
CData = zip(names,coordinates)


#need to update the popup function to select the correct name of the company/mine
def CreateMarkers(coordinates):
    for nm,co in CData:
        if len(str(co)) > 3:
            print(co)
            POI=geopy.Point(co)
            fg.add_child(folium.CircleMarker(location=[POI.latitude,POI.longitude],radius=6,popup=nm, fill_color = 'blue',color='blue',fill_opacity=0.6))
            map.add_child(fg)
#folium.map

data_file = 'african_railway_stations.osm'

"""e = xml.parse(data_file).getroot()
node_dict_tmp = {}
G = nx.DiGraph()
for i in e:
    if i.tag == "node":
        node_dict_tmp[i.attrib["id"]] = [i.attrib["lat"], i.attrib["lon"]]
        print(i)
        fg.add_child(folium.CircleMarker(location=[i.attrib["lat"],i.attrib["lon"]],radius=6,popup="station", fill_color = 'blue',color='blue',fill_opacity=0.6))
        map.add_child(fg)
"""
#For markers it is easier to create a feature gorup variable to control the look of the icon markers

#fg.add_child(folium.Marker(location=[-30.5,22.9],popup="This is the starting point", icon=folium.Icon(color='blue')))

map.add_child(folium.TileLayer(tiles='http://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png', attr="<a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>, '<a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA 2.0</a> <a href='http://www.openrailwaymap.org/'>OpenRailwayMap</a> and OpenStreetMap"))
#map.add_child(folium.
#map.add_child(folium.LayerControl())
#CreateMarkers(coordinates)

map.save("MapMarked.html")
