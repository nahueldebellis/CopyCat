import React from 'react';
import Link from 'next/link';
import Head from 'next/head';

class Inicio extends React.Component {
  render() {
    return(
		<div className="App">
				<Head>
					<title>CopyCat</title>
					<link rel="stylesheet" href="./index.css" />
				</Head>
				
				<h1 className="BIENVENIDOS">BIENVENIDOS</h1>
				<h2 className="NOSOTROS">NOSOTROS SOMOS</h2>
				<h3 className="COPYCAT">COPYCAT CORPORATION</h3>
				<Link href="/login">
					<span><input className="entrar" type="button" value="ENTRAR"/></span>
				</Link>
				<Link href="/register">
					<span><input className="unete" type="button" value="UNETE"/></span>
				</Link>
		</div>
    )
  }
}

export default Inicio;
