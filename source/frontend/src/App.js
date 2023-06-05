import './App.css';
import React from 'react';
import {Switch, Route, Link, NavLink} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Navbar';

import Billboard from './components/billboard';
import Profile from './components/profile';
import Login from './components/login';
import Signup from './components/signup';

function App() {
  const [user, setUser] = React.useState(null);
  const [token, setToken] = React.useState(null);
  const [error, setError] = React.useState('');

  async function login(user=null){
    setUser(user);
  }
  async function logout(user=null){
    setUser(null);
  }
  async function signup(user=null){
    setUser(user);
  }

  return (
    <div className="App">
        <Navbar className='navbar-bg' variant='dark'>
            <div className='container-fluid'>
                <Navbar.Brand>DevFuse</Navbar.Brand>
                    <Nav className='me-auto'>
                        <Container>
                            <Link class='nav-link' to={"/api/billboard/"}>Доска объявлений</Link>
                            { true ? (
                            <>
                                <Link class='nav-link' to={'/api/profile/'}>Мой профиль</Link>
                                <Link class='nav-link' to={'/token/logout/'}>Выйти, {user}</Link>
                            </>
                            ) : (
                            <>
                                <Link class='nav-link' to={'/token/login/'}>Войти</Link>
                                <Link class='nav-link' to={'/signup/'}>Регистрация</Link>
                            </>
                            )}

                        </Container>
                    </Nav>
            </div>
        </Navbar>

        <div className='container mt-4'>
            <Switch>
                // Billboard route
                <Route exact path={['/', '/api/billboard/']} render={(props) =>
                <Billboard {...props} token={token} />
                }>
                </Route>
                // Profile route
                <Route path='/api/profile/:id/' render={(props) =>
                <Profile {...props} token={token} />
                }>
                </Route>
                // Login router
                <Route path='/token/login/' render={(props) =>
                <Login {...props} login={login} />
                }>
                </Route>
                // Signup router
                <Route path='#' render={(props) =>
                <Signup {...props} signup={signup} />
                }>
                </Route>
            </Switch>
        </div>
    </div>
  );
}

export default App;
