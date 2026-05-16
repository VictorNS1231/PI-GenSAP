import requests
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

# CRIA O APP PRIMEIRO
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MODEL
class Pergunta(BaseModel):
    pergunta: str

# API KEY (sem quebra de linha)
API_KEY = "sua chave aqui"

# ROTA
@app.post("/chat")
def chat(data: Pergunta):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "nvidia/nemotron-3-super-120b-a12b:free",
                "messages": [
                    {
                        "role": "system",
                        "content": """
                Você é um especialista em SAP e banco de dados.

                Sempre responda nesse formato:

                Explicação:
                - explique de forma simples o que será feito

                SQL:
                - escreva apenas o SQL correto

                Use nomes comuns como:
                clientes(id, nome)
                vendas(id, cliente_id, valor, data)
                """
                    },
                    {
                        "role": "user",
                        "content": data.pergunta
                    }
                ]
            }
        )

        print(response.text)  # 👈 AQUI

        result = response.json()

        return {
            "resposta": result.get("choices", [{}])[0].get("message", {}).get("content", "Erro na IA")
        }

    except Exception as e:
        return {"resposta": f"Erro: {str(e)}"}