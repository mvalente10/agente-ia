# Arquivo principal do agente de IA
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

# Rota padrão para verificar se o servidor está ativo
@app.get("/")
def read_root():
    return {"message": "API está funcionando! Vá para /docs para ver a documentação"}

# Rota GET simples em /run-agent/
@app.get("/run-agent/")
def run_agent():
    return {"message": "Agente de IA em execução!"}

# Rota POST em /run-agent/ que aceita JSON
@app.post("/run-agent/")
async def run_agent_post(request: Request):
    try:
        data = await request.json()
        input_text = data.get("input", "Nenhuma entrada fornecida")
        return {"message": f"Agente processou o input: {input_text}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

