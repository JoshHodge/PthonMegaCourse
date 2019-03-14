import folium
map = folium.Map(location=[-30.5,22.9], zoom_start=6)
map.add_child(folium.Marker(location=[-30.5,22.9], popup="Starting Marker", icon=folium.Icon(color='green')))

map.save("Map1.html")
