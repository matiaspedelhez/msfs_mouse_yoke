import "./App.css";
import RightSide from "./components/RightSide/RightSide";
import LeftSide from "./components/LeftSide/LeftSide";
import BottomSide from "./components/BottomSide/BottomSide";
import { useState, useEffect } from "react";

function App() {
  const [controllerStatus, setControllerStatus] = useState({});
  const [logText, setLogText] = useState([]);

  useEffect(() => {
    // Update controller status based on listener from preload
    window.pythonStatus.status((event, data) => {
      const [status] = JSON.parse(data);
      setControllerStatus(status);
    });
  }, []);

  return (
    <div className="App">
      <img
        id="background"
        src="./assets/background.webp"
        alt="background"
      ></img>
      <div id="main-container">
        {/* logs, leftside, rightside */}
        <div id="top-section">
          <LeftSide />
          <RightSide controllerStatus={controllerStatus} />
        </div>
        <div id="bottom-section">
          <BottomSide />
        </div>
      </div>
    </div>
  );
}

export default App;
