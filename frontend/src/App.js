import './App.css';
import { Route } from 'react-router-dom';
import Tests from './Tests'
import Main from './Main'
import NavBar from './NavBar'
import TeststudentPre from './TeststudentPre'

function App() {
  return (
    <div className="App">
      <NavBar></NavBar>
      <Route exact path="/">
        <Main></Main>
      </Route>
      <Route exact path="/tests">
        <Tests></Tests>
      </Route>
      <Route path="/tests/students">
        <TeststudentPre></TeststudentPre>
      </Route>
    </div>
  );
}

export default App;
