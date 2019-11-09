import React from 'react';
import './Inicio.css';

class Inicio extends React.Component {
  render() {
    return(
      <div className="App">
        <h1 className="BIENVENIDOS">BIENVENIDOS</h1>
        <h2 className="NOSOTROS">NOSOTROS SOMOS</h2>
        <h3 className="COPYCAT">COPYCAT CORPORATION</h3>
        <span><input className="unete" type="button" value="UNETE"/></span>
        <span><input className="entrar" type="button" value="ENTRAR"/></span>

      </div>
    )
  }
}

export default Inicio;
