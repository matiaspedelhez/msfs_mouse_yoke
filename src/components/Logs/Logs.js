import "./Logs.css";
import { useState, useEffect } from "react";

function Logs() {
  const [logText, setLogText] = useState([]);

  useEffect(() => {
    // Update log data based on listener from preload
    window.logData.text((event, data) => {
      if (data) {
        setLogText((items) => [...items, data]);
      }
      console.log(logText);
    });
  }, []);

  return (
    <div>
      {logText.keys() &&
        logText.map((line, i) => {
          return <p key={i}>{line}</p>;
        })}
    </div>
  );
}

export default Logs;
