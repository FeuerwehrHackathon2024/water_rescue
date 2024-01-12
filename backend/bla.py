import folium
from geopy.distance import geodesic

center=(48.11043185557568, 11.556708643303125)

coords = [
    (48.12866391515209, 11.579115532906826),
    (48.12874450129121, 11.579304182296198),
    (48.12885530702604, 11.57950792363576),
    (48.1289711491296, 11.5798248546092),
    (48.12911217394705, 11.580096509728605),
    (48.12920283255335, 11.580285159117949),
    (48.12932371044619, 11.580503992408609),
    (48.12941940524348, 11.580692641797071),
    (48.12952517296921, 11.58085865325981),
    (48.12965108664446, 11.581100124477047),
    (48.12973670776722, 11.58128877386551),
    (48.129842474840075, 11.58146987727929),
    (48.12994320518254, 11.581620796790077),
    (48.130054008331086, 11.581801900203004),
    (48.13015977475044, 11.581990549592348),
    (48.130235449052634, 11.582149288540307),
    (48.130336178624276, 11.582337937928742),
    (48.13041172567341, 11.58247376548843),
    (48.130497345528596, 11.582617139024592),
    (48.13056281943875, 11.582752966584223),
    (48.13062829326543, 11.582911432070603),
    (48.13071391275898, 11.583069897557777),
    (48.13080456853771, 11.583243454995142),
    (48.1309002605756, 11.583417012432534),
    (48.13099091602538, 11.583590569870836),
    (48.1310916441152, 11.583771673283735),
    (48.13117222644482, 11.583952776696634),
    (48.1312628814151, 11.584126334134993),
    (48.1313384271009, 11.584262161694625),
    (48.131413972675574, 11.584382897303243),
    (48.13148951813909, 11.584541362789594),
    (48.13154995443048, 11.58465455242353),
    (48.13160535430123, 11.58478283400774),
    (48.13169600850628, 11.584956391445075),
    (48.131786662551264, 11.585077127053694),
    (48.13186724379025, 11.585190316687658),
    (48.131962933847944, 11.585341236198417),
    (48.13196797016178, 11.585341236198417)
 ]

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
            return index

end_index = get_end_index(283)

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