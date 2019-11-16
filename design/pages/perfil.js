import React, { useState, useEffect } from 'react';
import Router from 'next/router';



const Perfil = () =>  {
	const [nombre, setNombre] = useState('');
	const [apellido, setApellido] = useState('');
	const [email, setEmail] = useState('');

	function setState(data){
		setNombre(data['nombre']);
		setApellido(data['apellido']);
		setEmail(data['email']);
	}

	useEffect(()=>{
		fetch("http://localhost:88/welcome/user/", {
			credentials: 'include'
		})
		.then(res => res.json().then(data => setState(data)))
	})

    return( 
      	<div className="Perfil">
			
	      	<button type="button" onClick={() => Router.push('/reproductor')}>Reproductor</button>
      		<div className="Perfil">
				<h1 className="tit">Perfil</h1>
				<div className="Perfil2">
					<ul>
						<li>Nombre: {nombre}</li>
						<li>Apellido: {apellido}</li>
						<li>Email: {email}</li>						
					</ul>
				</div>
      		</div>
      	</div>
    )
}

export default Perfil;

