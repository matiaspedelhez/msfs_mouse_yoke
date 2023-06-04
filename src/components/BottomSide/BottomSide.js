import Logs from "../Logs/Logs";
import "./BottomSide.css";

function BottomSide(props) {
  return (
    <div className="BottomSide">
      <Logs log={props.log} />
    </div>
  );
}

export default BottomSide;
