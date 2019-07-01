import React, { Component } from 'react';
import logo from './logo.svg';
// import Element from './components/Elements/Element.js'
import PeriodicTable from './components/PeriodicTable/PeriodicTable.js'
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>

        <PeriodicTable />
        {/* <Element></Element> */}
      </div>
    );
  }
}

export default App;
