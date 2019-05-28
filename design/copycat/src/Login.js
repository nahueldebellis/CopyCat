import React from 'react';

class Login extends React.Component {
    render() {
      return(

        <form action="/welcome/login/" id="formulario1" method="POST">
          <div>  {/* <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} /> cuando se usa react, en las clases se le pone className*/}


            <input type="text" size="20" maxLength="30" placeholder="E-mail" name="email" autoComplete="off"/>
            <input type="password" size="20" maxLength="30" placeholder="Contraseña" name="contraseña" autoComplete="off" className="password"/> {/* cuando se usa react, en las clases se le pone className*/}
          {/*has olvidado tu comentario*/}
            <input type="submit" id="boton" onClick={validacion} value="Entrar"/>
           </div>
        </form>
      )
    }
}

exports.Login = Login;