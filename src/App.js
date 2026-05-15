import { useState } from "react";

function App() {
  const [pergunta, setPergunta] = useState("");
  const [resposta, setResposta] = useState("");

  const enviar = async () => {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        pergunta: pergunta
      })
    });

    const data = await res.json();
    setResposta(JSON.stringify(data.resposta, null, 2));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Chat IA</h1>

      <input
        value={pergunta}
        onChange={(e) => setPergunta(e.target.value)}
        placeholder="Digite sua pergunta"
      />

      <button onClick={enviar}>Enviar</button>

      <pre>{resposta}</pre>
    </div>
  );
}

export default App;