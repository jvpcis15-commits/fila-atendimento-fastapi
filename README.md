# fila-atendimento-fastapi

API de Fila de Atendimento

Esta API foi desenvolvida utilizando FastAPI e simula uma fila de atendimento com prioridade. É possível adicionar clientes, listar, remover e chamar o próximo da fila.

🚀 Tecnologias Utilizadas

Python 3.10+

FastAPI

Uvicorn

Pydantic

📁 Instalação e Execução
1️⃣ Clone o repositório (se aplicável)
git clone <url-do-repositorio>
cd <pasta-do-projeto>

2️⃣ Criar ambiente virtual
python -m venv venv

3️⃣ Ativar ambiente virtual
Windows (PowerShell):
venv\Scripts\activate

Linux / Mac:
source venv/bin/activate

4️⃣ Instalar dependências
pip install -r requirements.txt

5️⃣ Rodar a aplicação
uvicorn main:app --reload
