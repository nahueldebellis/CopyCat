import React from 'react';
import cokiee from './token';

class Register extends React.Component {
    constructor(){
        this.csrftoken = cokiee();
    }
    render() {

      return(
        <form action="/welcome/register/" id="formulario" method="POST">
            <div>
              <input type="hidden" name="csrfmiddlewaretoken" value={this.csrftoken} />
              <input type="text" size="20" maxLength="30" placeholder="Nombre" name="nombre" autoComplete="off" />
              <input type="text" size="20" maxLength="30" placeholder="Apellido" name="apellido" autoComplete="off"/>
              <input type="text" size="20" maxLength="30" placeholder="Fecha de nacimiento" name="fecha" autoComplete="off"/>
              <input type="email" size="20" maxLength="30" placeholder="E-mail" name="email" autoComplete="off"/>
              <input type="text" size="20" maxLength="30" placeholder="Genero" name="genero" autoComplete="off" />
              <input type="password" size="20" maxLength="30" placeholder="Contraseña" name="contraseña" autoComplete="off"/>
              <input type="password" size="20" maxLength="30" placeholder="Repetir Contraseña" name="repetir" autoComplete="off"/>
              <input type="submit" id="btn" onClick={validacion} value="Registrar"/>

            </div>

        </form>
      )
    }
}

exports.Register = Register;
