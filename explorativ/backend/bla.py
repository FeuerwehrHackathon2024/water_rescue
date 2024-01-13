import folium
import json
from geopy.distance import geodesic

center=(48.11043185557568, 11.556708643303125)

with open('../isar.json', 'r') as f:
    coords = json.load(f)

minutes = float(input("Geben Sie die Zeit in Minuten ein: "))

def get_distance(minutes):
    return 5.8*minutes*60

#sichtung = [48.129178372, 11.579766870]
sichtung = [48.129697542, 11.580641270]

def get_start_index(start_coord):
    dist = 9999999
    for index, coord in enumerate(coords):
        if geodesic(start_coord, coord).m <= dist:
            dist = geodesic(start_coord, coord).m
            pt = index + 1
    
    return pt

start_index = get_start_index(sichtung)

def get_end_index(meters):
    dist = 0
    for index in range(len(coords[start_index:])-1):
        index += start_index
        dist += geodesic(coords[index], coords[index+1]).m
        if meters <= dist:
            return index+1

end_index = get_end_index(get_distance(minutes))

# Karte erstellen
m = folium.Map(location=center, zoom_start=14)
colors = [i for i in range(len(coords))]
colors_2 = [i for i in range(len(coords[start_index:end_index]))]

folium.ColorLine(
    positions=coords,
    colors=colors,
    colormap=("cyan", "cyan"),
    weight=10,
).add_to(m)

folium.ColorLine(
    positions=coords[start_index:end_index],
    colors=colors_2,
    colormap=("green", "yellow", "red"),
    weight=10,
).add_to(m)

group_1 = folium.FeatureGroup("first group").add_to(m)
folium.Marker(sichtung, icon=folium.Icon("green")).add_to(group_1)
#folium.Marker(coords[end_index], icon=folium.Icon("red")).add_to(group_1)

m.save("index.html")