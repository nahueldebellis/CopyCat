import React from 'react';
import DjangoCSRFToken from 'django-react-csrftoken'
import Head from 'next/head';
class Login extends React.Component {
  constructor(){
    super();
  }
  render() {
    return(
      <div>
        <Head>
            <title>CopyCat</title>
            <link rel="stylesheet" href="./login.css" />
        </Head>
        <img src="fondo.jpg" alt="fondiu" id="fondex"/>
        <form action="http://localhost:88/welcome/login/" id="formulario" method="POST">
          <div id="contenedor">  
            <DjangoCSRFToken/>              
            <input type="text" size="20" maxLength="30" placeholder="E-mail" name="email" autoComplete="off" required="true" />
            <input type="password" size="20" maxLength="30" placeholder="Contraseña" name="password" autoComplete="off" className="password" required="true"/> {/* cuando se usa react, en las clases se le pone className*/}
            <input type="submit" id="entrar" value="Entrar"/>
          </div>
        </form>
      </div>
    )
  }
}

export default Login;