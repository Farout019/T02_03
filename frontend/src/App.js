import React, { useEffect, useState } from 'react';

function App() {
  const [mensaje, setMensaje] = useState('');

  useEffect(() => {
    // Realiza la petición al backend Flask
    fetch('http://127.0.0.1:5000/api/saludo')
      .then(response => response.json())
      .then(data => setMensaje(data.mensaje))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className="App">
      <h1>{mensaje}</h1>
    </div>
  );
}

export default App;
