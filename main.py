from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import logging


logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Sistema de Solicitações",
    description="MVP para registro e acompanhamento de solicitações internas",
    version="1.0"
)


solicitacoes = []


class Solicitacao(BaseModel):
    titulo: str
    descricao: str



@app.get("/")
def inicio():
    return {
        "mensagem": "Sistema de Solicitações funcionando"
    }



@app.post("/solicitacoes")
def criar_solicitacao(solicitacao: Solicitacao):

    
    for s in solicitacoes:
        if s["titulo"].lower() == solicitacao.titulo.lower():
            raise HTTPException(
                status_code=400,
                detail="Solicitação já cadastrada"
            )

    
    try:
        requests.get(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=5
        )
    except:
        logging.warning("Falha ao acessar API externa")

    nova = {
        "id": len(solicitacoes) + 1,
        "titulo": solicitacao.titulo,
        "descricao": solicitacao.descricao,
        "status": "Aberto"
    }

    solicitacoes.append(nova)

    logging.info(f"Solicitação criada: {nova['titulo']}")

    return nova



@app.get("/solicitacoes")
def listar_solicitacoes():
    return solicitacoes



@app.get("/solicitacoes/{id}")
def buscar_solicitacao(id: int):

    for s in solicitacoes:
        if s["id"] == id:
            return s

    raise HTTPException(
        status_code=404,
        detail="Solicitação não encontrada"
    )



@app.put("/solicitacoes/{id}/status")
def atualizar_status(id: int):

    for s in solicitacoes:
        if s["id"] == id:
            s["status"] = "Concluído"

            logging.info(
                f"Solicitação {id} concluída"
            )

            return s

    raise HTTPException(
        status_code=404,
        detail="Solicitação não encontrada"
    )