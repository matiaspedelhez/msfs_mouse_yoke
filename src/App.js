import './App.css';
import RightSide from './components/RightSide/RightSide';
import LeftSide from './components/LeftSide/LeftSide';
import BottomSide from './components/BottomSide/BottomSide';

function App() {
  return (
    <div className="App">
      <img id='background' src='./assets/background.webp' alt='background'></img>
      <div id='main-container'>
        {/* logs, leftside, rightside */}
        <div id='top-section'>
          <LeftSide />
          <RightSide />
        </div>
        <div id='bottom-section'>
          <BottomSide />
        </div>
        
      </div>
    </div>
  );
}

export default App;
