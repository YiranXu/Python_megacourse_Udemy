#Add dynamic colors for markers// change marker as circles
import folium
import pandas as pd
data=pd.read_csv("Volcanoes.txt")
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])
#dynamics color markers
def color_proceduer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<=3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=(38.58,-99.09),zoom_start=6,tiles = "Stamen Terrain")
fg=folium.FeatureGroup(name='My Map')

#add multiple markers
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=(lt,ln),popup=str(el)+'m',icon=folium.Icon(color=color_proceduer(el))))
    #fg.add_child(folium.CircleMarker(location=(lt,ln),radius=6,popup=str(el)+'m',
    #fill_color=color_proceduer(el),color='grey',fill_opacity=0.7))
map.add_child(fg)

map.save('Map2_color.html')    