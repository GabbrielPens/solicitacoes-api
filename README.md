Sistema de Solicitações Internas
Integrantes

Gabriel Adroaldo da Rocha Pens

Hadryan Porcino dos Santos

Objetivo
Sistema para registro e acompanhamento de solicitações internas de TI, manutenção e suporte.

Tecnologias
Python

FastAPI

Requests

Uvicorn

Endpoints
Criar solicitação
POST /solicitacoes

Listar solicitações
GET /solicitacoes

Buscar solicitação por ID
GET /solicitacoes/{id}

Atualizar status
PUT /solicitacoes/{id}/status

Como executar
Instalar dependências:

pip install -r requirements.txt

Executar:

uvicorn main:app --reload

Abrir:

http://127.0.0.1:8000/docs

Links para acesso: 

https://solicitacoes-api.onrender.com
https://solicitacoes-api.onrender.com/docs#/
https://github.com/GabbrielPens/solicitacoes-api/tree/main
