import React from 'react';
import ReactDOM from 'react-dom';

import Register from './Register/Register';
import Login from './Login/Login';
import Reproductor from './Reproductor/Reproductor';
import * as serviceWorker from './serviceWorker';
ReactDOM.render(<Reproductor />, document.getElementById('root'));


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
