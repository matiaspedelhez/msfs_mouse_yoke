import "./ConfigurationButtonNumberSelector.css";
import { useState, useRef } from "react";

function ConfigurationButtonNumberSelector(props) {
  const [value, setValue] = useState({ value: "" });
  const inputField = useRef(null);

  const handleSetValue = (event) => {
    let eventValue = event.target.value;
    const maxLength = 3;

    // event value exists, its type's string and its length is less than max
    if (
      // (eventValue || eventValue === "") &&
      typeof eventValue === "string" &&
      eventValue.length <= maxLength
    ) {
      // setValue({ value: eventValue.match(/\d+/) });
      // callback to python function props.callback
      //
    }
    console.log(eventValue.match(/\d+/));
  };

  const placeCursorAtTheEnd = (elementRef) => {
    let lenght = 0;
    if (elementRef.current.value) {
      lenght = elementRef.current.value;
    }
    elementRef.current.setSelectionRange(lenght, lenght);
  };

  return (
    <div className="ConfigurationButtonNumberSelector">
      <p className="short-description">{props.shortDescription}</p>
      <div>
        <input
          className="input-field"
          ref={inputField}
          value={value.value}
          onChange={(e) => handleSetValue(e)}
          onClick={() => placeCursorAtTheEnd(inputField)}
        />
      </div>
    </div>
  );
}

export default ConfigurationButtonNumberSelector;
