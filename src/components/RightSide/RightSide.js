import "./RightSide.css";
import StatusBar from "../StatusBar/StatusBar";
function RightSide(props) {
  return (
    <div className="RightSide">
      <div className="title">
        <p>{"> "}LIVE STATUS</p>
      </div>
      <div className="right-side-items">
        <StatusBar
          name="MOUSE X"
          controller_data={
            props.controllerStatus.data
              ? props.controllerStatus.data.transformed_x
              : ""
          }
        />
        <StatusBar
          name="MOUSE Y"
          controller_data={
            props.controllerStatus.data
              ? props.controllerStatus.data.transformed_y
              : ""
          }
        />
        <StatusBar
          name="MOUSE WHEEL"
          controller_data={
            props.controllerStatus.data
              ? props.controllerStatus.data.transformed_wheel
              : ""
          }
        />
      </div>
    </div>
  );
}

export default RightSide;
