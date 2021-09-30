import folium
import pandas as pd
data=pd.read_csv("Volcanoes.txt")
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])
name = list(data["NAME"])
#add HTML to make stylized popup texts
html = """<h4>Volcano information:</h4>
Height: %s m
"""
html2 = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map=folium.Map(location=(38.58,-99.09),zoom_start=6,tiles = "Stamen Terrain")
fg=folium.FeatureGroup(name='My Map')

#add multiple markers
for lt,ln,el,name in zip(lat,lon,elev,name):
    #iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    iframe = folium.IFrame(html=html2 % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=(lt,ln),popup=folium.Popup(iframe),icon=folium.Icon(color='green')))
map.add_child(fg)
map.save('Map_html_popup_advanced1.html')    