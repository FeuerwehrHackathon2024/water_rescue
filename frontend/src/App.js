import Paper from '@mui/material/Paper';
import MapWithPolygon from "./components/MapWithPolygon";
import Slider from '@mui/material/Slider';

import Button from '@mui/material/Button';
import {useState} from "react";

function App() {
    const [allowSetMarkers, setAllowSetMarkers] = useState(false)
    const [buttonName, setButtonName] = useState("Setze Startpunkt")
    const [inputMinutes, setInputMinutes] = useState(5)
    const [inputLevel, setInputLevel] = useState(50)

    const handleInputChange = (event) => {
        setInputMinutes(event.target.value);
    };
    const handleLevelChange = (event) => {
        setInputLevel(event.target.value);
    };

    const handleToggle = () => {
        setAllowSetMarkers(!allowSetMarkers);

        if (!allowSetMarkers)
        {
            setButtonName("Entferne Startpunkt")
        } else {
            setButtonName("Setze Startpunkt")
        }
    };

  return (
    <div >
        <Paper style={{width:"60vw", height:"90vh"}}>
            <Button variant="contained" onClick={handleToggle}>{buttonName}</Button>
            <p>Minuten</p>
            <Slider min={0} max={70} onChange={handleInputChange} step={5} valueLabelDisplay="auto"/>
            <p>Pegelstand</p>
            <Slider min={50} max={350} step={5} onChange={handleLevelChange} valueLabelDisplay="auto"/>
            <MapWithPolygon setMarkers={allowSetMarkers} minutes={inputMinutes} level={inputLevel}/>
        </Paper>
    </div>
  );
}

export default App;
