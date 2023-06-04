import "./StatusBar.css";
import { useState, useEffect } from "react";

function StatusBar(props) {
  const [transformedValue, setTransformedValue] = useState("");
  useEffect(() => {
    // Value gets in as -1 (0) to 1 (100) float
    const value = props.controller_data;
    let transformedVal = 0;
    if (value || value === 0) {
      transformedVal = ((value + 1) / 2) * 100;
      setTransformedValue(transformedVal);
    }
  }, [props.controller_data]);

  return (
    <div className="status-bar">
      <p className="status-bar-name">{props.name}</p>
      <hr />
      <div className="status-bar-progress">
        <div className="bar" style={{ width: `${transformedValue}%` }}></div>
      </div>
    </div>
  );
}

export default StatusBar;
