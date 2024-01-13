import React, {useState} from 'react';
import LocationOnIcon from "../assets/maps-flags_447031.png";
import L from "leaflet";
import {Marker, useMapEvents} from "react-leaflet";

function LocationMarkers(props) {

    const initialMarkers = null;
    const [marker, setMarker] = useState(initialMarkers);

    const pingIconOptions = {
        iconUrl: LocationOnIcon,
        iconSize: [32, 32], // Set the size of the icon
        iconAnchor: [16, 32], // Set the anchor point for the icon (half of the icon size)
        popupAnchor: [0, -32], // Set the popup anchor point (above the icon)
    };

    const pingMarker = L.icon(pingIconOptions);

    const map = useMapEvents({
        click(e) {
            if (props.setMarkersAllowed === true){
                setMarker(e.latlng);
                props.locRef(e.latlng)
                console.log(e)
            }
        }
    });

    return (
        <div>
            {
                marker ? <Marker position={marker} icon={pingMarker}></Marker> : <div></div>
            }
        </div>
    );
}

export default LocationMarkers;