import { useState } from "react";

function App() {
  const [pergunta, setPergunta] = useState("");
  const [resposta, setResposta] = useState("");

  const enviar = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ pergunta })
      });

      const data = await res.json();
      setResposta(data.resposta);
    } catch (erro) {
      setResposta("Erro ao conectar com o backend ❌");
      console.error(erro);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Chat IA 🚀</h1>

      <input
        value={pergunta}
        onChange={(e) => setPergunta(e.target.value)}
        placeholder="Digite sua pergunta"
      />

      <button onClick={enviar}>Enviar</button>

      <div style={{ whiteSpace: "pre-wrap" }}>
        {resposta}
      </div>
    </div>
  );
}

export default App;