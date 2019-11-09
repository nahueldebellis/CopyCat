import React from 'react';
import fondo from './fondo.jpg';
import './login.css';
import DjangoCSRFToken from 'django-react-csrftoken'

class Login extends React.Component {
    constructor(){
      super();
      
    }
    render() {
      return(
        <div>
          <img src={ fondo } alt="fondiu" id="fondex"/>
          <form action="http://localhost:88/welcome/login/" id="formulario" method="POST">
            <div id="contenedor">  
              <DjangoCSRFToken/>              
              <input type="text" size="20" maxLength="30" placeholder="E-mail" name="email" autoComplete="off" required="true" />
              <input type="password" size="20" maxLength="30" placeholder="Contraseña" name="password" autoComplete="off" className="password" required="true"/> {/* cuando se usa react, en las clases se le pone className*/}
              {/*has olvidado tu contraseña*/}
              <input type="submit" id="entrar" value="Entrar"/>
            </div>
          </form>
        </div>
      )
    }
}

export default Login;