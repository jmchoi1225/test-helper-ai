import './App.css';
import { Route } from 'react-router-dom';
import Tests from './Tests'
import Main from './Main'
import NavBar from './NavBar'
import TestStudentPre from './TestStudentPre'

function App() {
  return (
    <div className="App">
      <NavBar></NavBar>
      <Route exact path="/" component={Main} />
      <Route exact path="/tests" component={Tests} />
      <Route path="/tests/students" component={TestStudentPre} / >
    </div>
  );
}

export default App;
