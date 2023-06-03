import "./ConfigurationButtonKeySelector.css";
import { useState, useRef } from "react";

function ConfigurationButtonKeySelector(props) {
  const [key, setKey] = useState({ value: "" });
  const inputField = useRef(null);

  const handleSetKey = (event) => {
    let eventValue = event.nativeEvent.data;

    // event value exists, its type's string and its different than before
    if (
      eventValue &&
      typeof eventValue === "string" &&
      key.value !== eventValue
    ) {
      eventValue = eventValue.toLowerCase();
      setKey({ value: eventValue });
      // callback to python function props.callback
    }

    inputField.current.blur();
  };

  return (
    <div className="ConfigurationButtonKeySelector">
      <p className="short-description">{props.shortDescription}</p>
      <div>
        <input
          className="input-field"
          ref={inputField}
          value={key.value}
          onChange={(e) => handleSetKey(e)}
        />
      </div>
    </div>
  );
}

export default ConfigurationButtonKeySelector;
