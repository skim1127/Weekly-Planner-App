import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

// COMPONENTS
import Home from './components/Home'

function App() {
  return (
    <div className="App">
      <Router>
        <div className="display">
          <Routes>
            <Route path="/" element={ <Home/> }/>
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
