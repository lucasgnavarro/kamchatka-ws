import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import IndexMobile from './mobile';
import AudioView from './mobile/audio';
import Manager from './manager';

import logo from './logo.svg';
import './App.css';

const NoMatch = () => <div><h1>404</h1></div>

const RedirectManager = () => {
  if((typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1)){
    return (<Redirect to="/client" />);
  }else{
    return (<Redirect to="/manager" />);
  }
}

const App = () => {
  const someVariable = true;
  
  return (
    <Switch>
      {/* these are good */}
      <Route exact path='/' component={RedirectManager} />
      
      <Route path='/client' component={IndexMobile}>
        <Route path='/client/audio/' component={AudioView} />
      </Route>

      <Route exact path='/manager' component={Manager} />
      <Route component={NoMatch}/>
      
      {/* <Route
        path='/about'
        render={(props) => <About {...props} extra={someVariable} />}
      /> */}
      
    </Switch>
  )
}
/* 
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
} */

export default App;
