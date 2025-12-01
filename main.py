from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(title="API de Fila de Atendimento")

# Modelo de entrada
class ClienteEntrada(BaseModel):
    nome: str = Field(..., max_length=20)
    tipo_atendimento: str = Field(..., min_length=1, max_length=1, pattern="^(N|P)$")

# Base de dados temporária
fila = []


# Atualiza posições
def atualizar_posicoes():
    for index, cliente in enumerate(fila):
        cliente["posicao"] = index + 1


# GET /fila
@app.get("/fila")
def listar_fila():
    return fila if len(fila) > 0 else []


# POST /fila
@app.post("/fila")
def adicionar_cliente(cliente: ClienteEntrada):
    novo = {
        "posicao": len(fila) + 1,
        "nome": cliente.nome,
        "tipo_atendimento": cliente.tipo_atendimento,
        "data_chegada": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "atendido": False
    }

    # inserção com prioridade
    if cliente.tipo_atendimento == "P":
        index = next((i for i, c in enumerate(fila) if c["tipo_atendimento"] == "N"), len(fila))
        fila.insert(index, novo)
    else:
        fila.append(novo)

    atualizar_posicoes()  # sempre recalcular
    return {"mensagem": "Cliente adicionado com sucesso!", "cliente": novo}


# GET /fila/{id}
@app.get("/fila/{id}")
def obter_cliente(id: int):
    if id < 1 or id > len(fila):
        raise HTTPException(status_code=404, detail="Cliente não encontrado nessa posição.")
    return fila[id - 1]


# DELETE /fila/{id}
@app.delete("/fila/{id}")
def remover_cliente(id: int):
    if id < 1 or id > len(fila):
        raise HTTPException(status_code=404, detail="Cliente não localizado.")

    fila.pop(id - 1)
    atualizar_posicoes()
    return {"mensagem": "Cliente removido com sucesso", "fila_atual": fila}


# PUT /atender
@app.put("/atender")
def atender_proximo():
    if not fila:
        return {"mensagem": "Não há clientes na fila para atualizar"}

    fila[0]["posicao"] = 0
    fila[0]["atendido"] = True
    atendido = fila.pop(0)

    atualizar_posicoes()

    return {"mensagem": "Cliente chamado para atendimento", "cliente": atendido}