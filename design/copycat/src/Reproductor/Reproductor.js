import React from 'react';
import cokiee from '../Token';
//import fondo from './fondo.jpg';
///import { Link, withRouter } from 'react-router-dom';
/* <audio id="miAudio" src="parte1.mp3"></audio> */
class Reproductor extends React.Component {
  constructor(){
    super();
    this.duracion = 0;
    this.interval = 10;
    this.miAudio=document.getElementById("miAudio");
    this.csrftoken = cokiee;
  }

  iniciar(){
      if(this.miAudio !== null){
        if(this.miAudio.paused){
            this.miAudio.play();
            this.interval=setInterval(this.mostrarDuracion,100);
            document.getElementById("iniciar").innerHTML="&#8545;";
        }
        else{
            this.miAudio.pause();
            clearInterval(this.interval);
            document.getElementById("iniciar").innerHTML="&#8227;";
        }
      }
        else
            console.log('nno');


  }

  reiniciar(){
    if(this.miAudio !== null){
      this.miAudio.play();
      this.interval=setInterval(this.mostrarDuracion,100);
    }
    else
        console.log('no')

  }


  mostrarDuracion(){
    if(this.duracion>0)
    {
      this.porcentaje=this.miAudio.currentTime*100/this.duracion;
      document.getElementById("duracion").getElementsByTagName("span")[0].style.width=this.porcentaje+"px";
      document.getElementById("duracion").getElementsByTagName("div")[0].innerHTML=parseInt(this.porcentaje)+"%";
    }
  }


  render() {
    return(
      <div id="divcontenedor"> {/*sin este div, el programa no funciona*/}
        <audio id="miAudio" src="parte1.mp3"></audio>
          <div id="duracion"></div>
            <span></span>
            <div></div>
          <div id="botones">
            <button id="iniciar" onClick={this.iniciar()}>&#8227;</button>
            <button id="reiniciar" onClick={this.reiniciar()}>&#8635;</button>
          </div>
      </div>
    );
  }
}


export default Reproductor;
