import Inicio from './inicio'
import Head from 'next/head';
const App = ()=>(
    <div>
        <Head>
            <title>CopyCat</title>
            <link rel="stylesheet" href="./index.css" />
        </Head>
        <Inicio/>
    </div>
)

export default App;