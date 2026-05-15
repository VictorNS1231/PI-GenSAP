import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pergunta(BaseModel):
    pergunta: str

@app.post("/chat")
def chat(data: Pergunta):

    resposta = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "nvidia/nemotron-3-super-120b-a12b:free",
            "messages": [
                {
                    "role": "user",
                    "content": data.pergunta
                }
            ]
        }
    )

    resultado = resposta.json()

    print(resultado)

    if "choices" not in resultado:
        return {
            "erro": resultado
        }

    return {
        "resposta": resultado["choices"][0]["message"]["content"]
    }