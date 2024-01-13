import coords from "../assets/isar.json"

function haversine(startCoord, endCoord) {
  // Radius der Erde in Metern
  const R = 6371e3;

  // Konvertierung der Koordinaten von Grad in Radian
  const lat1Rad = startCoord[0] * (Math.PI / 180);
  const lon1Rad = startCoord[1] * (Math.PI / 180);
  const lat2Rad = endCoord[0] * (Math.PI / 180);
  const lon2Rad = endCoord[1] * (Math.PI / 180);

  // Deltas der Koordinaten
  const dlat = lat2Rad - lat1Rad;
  const dlon = lon2Rad - lon1Rad;

  // Haversine-Formel
  const a = Math.sin(dlat / 2) ** 2 + Math.cos(lat1Rad) * Math.cos(lat2Rad) * Math.sin(dlon / 2) ** 2;
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  // Berechnung des Abstands
  const distance = R * c;

  return distance;
}

const WATER_DATA = {
  50: 0.95,
  75: 1.25,
  100: 1.45,
  125: 1.61,
  150: 1.74,
  175: 1.86,
  200: 1.96,
  225: 2.06,
  250: 2.14,
  275: 2.22,
  300: 2.3,
  325: 2.37,
  350: 2.43,
};

export function getDistance(minutes, level) {
  return 5.8 * minutes * 60;
}


export function getStartIndex(startCoord) {
  let dist = 9999999;
  let pt = -1;

  for (let index = 0; index < coords.length; index++) {
    const coord = coords[index];
    const distance = haversine(startCoord, coord);

    if (distance <= dist) {
      dist = distance;
      pt = index + 1;
    }
  }

  return pt;
}

export function getEndIndex(meters, startIndex) {
  let dist = 0;

  for (let index = startIndex; index < coords.length - 1; index++) {
    dist += haversine(coords[index], coords[index + 1]);

    if (meters <= dist) {
      return index + 1;
    }
  }

  return -1; // Rückgabewert, falls die Distanz nicht erreicht wurde
}
