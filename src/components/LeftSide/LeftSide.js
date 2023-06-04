import ConfigurationButtonKeySelector from "../ConfigurationButtonKeySelector/ConfigurationButtonKeySelector";
import ConfigurationButtonNumberSelector from "../ConfigurationButtonNumberSelector/ConfigurationButtonNumberSelector";
import "./LeftSide.css";

function LeftSide() {
  return (
    <div className="LeftSide">
      <div className="title">
        <p>{"> "}MOUSEYOKE MSFS</p>
      </div>
      <div className="configutaration-items">
        <ConfigurationButtonKeySelector
          shortDescription={"ON/OFF KEYBIND"}
          callback={{}}
        />
        <ConfigurationButtonKeySelector
          shortDescription={"CENTER AXIS KEYBIND"}
          callback={{}}
        />
        <ConfigurationButtonNumberSelector
          shortDescription={"THROTTLE SENSITIVITY"}
          callback={{}}
        />
        <button onClick={() => window.pythonFunctions.requestRun()}>
          Start
        </button>
      </div>
    </div>
  );
}

export default LeftSide;
