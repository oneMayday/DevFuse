import './App.css';
import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import Billboard from './components/billboard';
import Profile from './components/profile';
import Login from './components/login';
import Signup from './components/signup';

function App() {
  return (
    <div className="App">
    <Navbar bg='primary' variant='dark'>
    <div className='container-fluid'>
    <Navbar.Brand>React-bootstrap</Navbar.Brand>
    <Nav className='me-auto'>
    <Nav.Link href='#home'>Home</Nav.Link>
    <Nav.Link href='#link'>Link</Nav.Link>
    </Nav>
    </div>
    </Navbar>
      Hello world
    </div>
  );
}

export default App;
