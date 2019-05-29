import React from 'react';
import cokiee from '../Token';
import fondo from './fondo.jpg';
import './register.css';

class Register extends React.Component {
    constructor(){
      super();
      this.csrftoken = cokiee;
    }

    validacion(){
      var formulario = document.getElementById('formulario');
      var elementos = formulario.elements;

      var validarRepeticion = function(e){
        if (elementos.contraseña.value != elementos.repetir.value) {
          alert("Las passwords deben de coincidir");
          e.preventDefault(e);
        }
      }

      formulario.addEventListener("submit", validarRepeticion);
    }

    render() {
      return(
        <div>
          <img src={fondo} alt="fondiu" id="fondex"></img>
          <form action="/welcome/register/" id="formulario" method="POST">
              <div id="contenedor">
                <input type="hidden" name="csrfmiddlewaretoken" value={this.csrftoken} />
                <input type="text" size="20" maxLength="30" placeholder="Nombre" name="nombre" autoComplete="off" required="true" />
                <input type="text" size="20" maxLength="30" placeholder="Apellido" name="apellido" autoComplete="off" required="true" />
                <input type="text" size="20" maxLength="30" placeholder="Fecha de nacimiento" name="fecha" autoComplete="off" required="true" />
                <input type="email" size="20" maxLength="30" placeholder="E-mail" name="email" autoComplete="off" required="true" />
                <input type="text" size="20" maxLength="30" placeholder="Genero" name="genero" autoComplete="off" required="true" />
                <input type="password" size="20" maxLength="30" placeholder="Contraseña" name="contraseña" autoComplete="off" required="true" />
                <input type="password" size="20" maxLength="30" placeholder="Repetir Contraseña" name="repetir" autoComplete="off" required="true" />
                <input type="submit" id="register" onClick={this.validacion} value="Registrar"/>

              </div>

          </form>
        </div>
      )
    }
}

export default Register;
