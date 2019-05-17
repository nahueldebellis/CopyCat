import React from 'react';
import './App.css';

class Register extends React.Component {
  render() {
    return(
      <form action="http://localhost/welcome/register/" method="POST">
        <div>
          
          <input type="text" size="20" maxlength="30" placeholder="Nombre" name="nombre" autoComplete="off" />
          <input type="text" size="20" maxlength="30" placeholder="Apellido" name="apellido" autoComplete="off"/>
          <input type="text" size="20" maxlength="30" placeholder="Fecha de nacimiento" name="date" autoComplete="off"/>
          <input type="text" size="20" maxlength="30" placeholder="E-mail" name="email" autoComplete="off"/>
          <input type="text" size="20" maxlength="30" placeholder="Gender" name="genero" autoComplete="off" />
          <input type="password" size="20" maxlength="30" placeholder="Contraseña" name="password" autoComplete="off"/>
          <input type="password" size="20" maxlength="30" placeholder="Repetir Contraseña" name="repetircontraseña" autoComplete="off"/>
          
          <input type='submit' value="Submit" />


        </div>

      </form>
    );
  }
}

export default Register;
