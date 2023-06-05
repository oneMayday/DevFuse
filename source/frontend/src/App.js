import './App.css';
import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Navbar';

import Billboard from './components/billboard';
import Profile from './components/profile';
import Login from './components/login';
import Signup from './components/signup';

function App() {
  const user = null;
  return (
    <div className="App">
        <Navbar className='navbar-bg' variant='dark'>
            <div className='container-fluid'>
                <Navbar.Brand>DevFuse</Navbar.Brand>
                    <Nav className='me-auto'>
                        <Container>
                            <Link class='nav-link' to={"/api/billboard"}>Доска объявлений</Link>
                            { true ? (
                            <Link class='nav-link'>Logout ({user})</Link>
                            ) : (
                            <>
                                <Link class='nav-link' to={'/login'}>Login</Link>
                                <Link class='nav-link' to={'/signup'}>Signup</Link>
                            </>
                            )}
                        </Container>
                    </Nav>
            </div>
        </Navbar>
        Hello world
    </div>
  );
}

export default App;
