import React, {useEffect, useState} from 'react';
import {MapContainer, TileLayer, Polyline} from 'react-leaflet';
import 'leaflet/dist/leaflet.css'
import isar_data from "../assets/isar.json"
import LocationMarkers from "./LocationMarkers";

import {getStartIndex, getDistance, getEndIndex} from "./route"

const MapWithPolygon = (props) => {
    const mapCenter = [48.137400361036555, 11.57670136034838];
    const [personTrail, setPersonTrail] = useState([])
    const [lastLoc, setLastLoc] = useState()

    const handleLoc = (targetLoc) => {
        if (targetLoc)
        {
            setLastLoc(targetLoc)
            const distance = getDistance(props.minutes, props.level)

            const startIndex = getStartIndex([targetLoc.lat, targetLoc.lng])
            const endIndex = getEndIndex(distance, startIndex)

            setPersonTrail(isar_data.slice(startIndex, endIndex))
        }
    }

    useEffect(() => {
        handleLoc(lastLoc)
    }, [handleLoc, lastLoc, props.minutes]);

    useEffect(() => {
        if (!props.setMarkers) {
            setPersonTrail([])
            setLastLoc(null)
        }
    }, [props.setMarkers]);

    return (
        <MapContainer center={mapCenter} zoom={13}
                      style={{ height: '60%', width: '100wh' }}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Polyline
                positions={isar_data}
                color="blue"
                fillColor="blue"
                fillOpacity={1}
                weight={10}
            />

            <Polyline
                positions={personTrail}
                color="green"
                fillColor="blue"
                fillOpacity={1}
                weight={10}
            />
            {
                props.setMarkers ? <LocationMarkers setMarkersAllowed={props.setMarkers} locRef={handleLoc}/> : <></>
            }
        </MapContainer>
    );
};

export default MapWithPolygon;
