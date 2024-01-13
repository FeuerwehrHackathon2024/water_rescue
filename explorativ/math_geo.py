import math

def haversine(lat1, lon1, lat2, lon2):
    # Ermittlung der Entfernung zwischen zwei Punkten
    R = 6371 # Erddurchmesser in km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d

# Beispielverwendung:

# Kartenkoordinaten (latitude, longitude) von Punkt A und Punkt B
point_a = (48.858093, 2.294694) # Eiffelturm
point_b = (40.7128, -74.0060) # Statue der Freiheit

# Berechnung der Entfernung
distance = haversine(point_a[0], point_a[1], point_b[0], point_b[1])

print("Die Entfernung zwischen den beiden Punkten beträgt: ", distance, "Kilometer")