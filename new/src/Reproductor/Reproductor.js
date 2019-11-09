import React from 'react';
import beatles from './beatles.jpg';
import "./reproductor.css";
//import { Link, withRouter } from 'react-router-dom';


class Reproductor extends React.Component {

	constructor(props) {
			super(props);
			this.cleanUrl = "http://localhost:8000/reproductor/player/";
			this.state = {
				url: "http://localhost:8000/reproductor/player/",
				buscador: "",
				name: "",
				author: "",
				album: "",
			};
			this.play= this.play.bind(this);
	}

	busqueda(text){
		this.setState({buscador: text})    
	}
	
	play(){
		fetch("http://localhost:8000/reproductor/search/"+this.state.buscador)
		.then(res => res.json().then( data => this.setState({ 
			url: this.cleanUrl+data[0][0],
			name: data[0][1],
			album: data[0][2],
			author: data[0][3]
		})))
		.then(() => {
			let audio = document.getElementById('audio');
			audio.load();
			audio.play();
		})
	}

	render() {
		
		return (
			<div className="center">
				<div className="row d-flex justify-content-center form-group">
					<input className="col-sm-6 form-control" type="text" onChange={e=>this.busqueda(e.target.value)} value={this.state.buscador}/>
					<button className="col-sm-2 btn btn-secondary" onClick={this.play}>
						Search
					</button>
				</div>
				<img src={ beatles } className="img"/>
				<h1 className="h1">{ this.state.name }</h1>
				<h2 className="h2"> { this.state.author } </h2>
				<audio controls id="audio" className="repro">
					<source src={this.state.url} type="audio/wav"/>
				</audio>
			</div>
		);
	}
}



export default Reproductor;

