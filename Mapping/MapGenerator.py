import folium
map = folium.Map(location=[-30.5,22.9], zoom_start=6)
# map.add_child(folium.Marker(location=[-30.5,22.9],popup="This is the starting point", icon=folium.Icon(color='blue')))

#For markers it is easier to create a feature gorup variable to control the look of the icon markers
fg= folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[-30.5,22.9],popup="This is the starting point", icon=folium.Icon(color='blue')))
map.add_child(fg)

map.save("MapMarked.html")
