from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date


app = FastAPI()

class CadastroProduto(BaseModel):
    NF: str
    fornecedor: str
    cidade: str
    cliente: str
    quantidade_total: int
    data_criacao: date



@app.post("/enviar-dados/")
async def enviar_dados(dados: CadastroProduto):
    response = {
        "status": "sucesso",
        "mensagem": "Dados recebidos e processados.",
        "dados": dados.dict()
    }
    return response